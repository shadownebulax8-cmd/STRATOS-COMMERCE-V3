import os
from typing import Any, Dict

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from stratos_commerce_core.core.tenant_policy import TenantPolicy


class MultiTenantSessionRouter:
    """Maps tenant identifiers to isolated database connections."""

    def __init__(self) -> None:
        self.engines_pool: Dict[str, Any] = {}
        self.base_db_url = os.getenv(
            "DATABASE_BASE_URL",
            "postgresql+asyncpg://postgres:postgres@localhost:5432/",
        )
        self.policy = TenantPolicy()

    def get_tenant_connection_string(self, tenant_id: str) -> str:
        if not self.policy.validate_tenant(tenant_id):
            raise ValueError(f"Unsupported tenant: {tenant_id}")
        tenant_name = tenant_id.replace("-", "_")
        return f"{self.base_db_url}tenant_{tenant_name}"

    async def get_tenant_session(self, tenant_id: str) -> AsyncSession:
        if tenant_id not in self.engines_pool:
            connection_url = self.get_tenant_connection_string(tenant_id)
            engine = create_async_engine(connection_url, pool_size=10, max_overflow=20)
            self.engines_pool[tenant_id] = sessionmaker(
                bind=engine,
                class_=AsyncSession,
                expire_on_commit=False,
            )

        session_factory = self.engines_pool[tenant_id]
        return session_factory()
