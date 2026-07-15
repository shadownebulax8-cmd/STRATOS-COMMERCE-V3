from typing import Dict, Optional


class TenantPolicy:
    """Central policy for tenant-specific routing and access control."""

    def __init__(self) -> None:
        self.allowed_tenants: Dict[str, str] = {
            "alpha": "tenant_alpha",
            "beta": "tenant_beta",
            "gamma": "tenant_gamma",
        }

    def resolve_tenant_schema(self, tenant_id: str) -> Optional[str]:
        return self.allowed_tenants.get(tenant_id)

    def validate_tenant(self, tenant_id: str) -> bool:
        if tenant_id in self.allowed_tenants:
            return True
        return len(tenant_id) > 2 and tenant_id.replace("-", "").replace("_", "").isalnum()
