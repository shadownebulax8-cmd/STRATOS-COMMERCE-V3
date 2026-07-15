import unittest

from stratos_commerce_core.auth.jwt_auth import create_access_token, verify_token
from stratos_commerce_core.core.tenant_manager import MultiTenantSessionRouter
from stratos_commerce_core.pipeline.schemas import MerchantCreateRequest


class MVPFeatureTests(unittest.TestCase):
    def test_token_round_trip(self) -> None:
        token = create_access_token(sub="merchant-1", role="merchant_admin", tenant_id="alpha")
        payload = verify_token(token)
        self.assertEqual(payload["sub"], "merchant-1")
        self.assertEqual(payload["role"], "merchant_admin")
        self.assertEqual(payload["tenant_id"], "alpha")

    def test_tenant_schema_name_is_stable(self) -> None:
        router = MultiTenantSessionRouter()
        self.assertEqual(router.get_tenant_connection_string("acme"), "postgresql+asyncpg://postgres:postgres@localhost:5432/tenant_acme")

    def test_merchant_create_schema_validates(self) -> None:
        payload = MerchantCreateRequest(tenant_id="acme", legal_name="Acme Industries", subdomain="acme")
        self.assertEqual(payload.tenant_id, "acme")
        self.assertEqual(payload.subdomain, "acme")


if __name__ == "__main__":
    unittest.main()
