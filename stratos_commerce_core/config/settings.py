import os
from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class Settings:
    project_name: str = os.getenv("PROJECT_NAME", "STRATOS-COMMERCE V3")
    environment: str = os.getenv("ENVIRONMENT", "development")
    debug: bool = os.getenv("DEBUG", "true").lower() == "true"
    database_base_url: str = os.getenv(
        "DATABASE_BASE_URL",
        "postgresql+asyncpg://postgres:postgres@localhost:5432/",
    )
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    celery_broker_url: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/1")
    celery_result_backend: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/2")
    stripe_secret_key: str = os.getenv("STRIPE_SECRET_KEY", "sk_test_placeholder")
    platform_fee_percent: float = float(os.getenv("PLATFORM_FEE_PERCENT", "2.5"))
    tenant_subdomain_map: Dict[str, str] = None

    def __post_init__(self) -> None:
        if self.tenant_subdomain_map is None:
            object.__setattr__(
                self,
                "tenant_subdomain_map",
                {
                    "alpha": "tenant_alpha",
                    "beta": "tenant_beta",
                    "gamma": "tenant_gamma",
                },
            )


settings = Settings()
