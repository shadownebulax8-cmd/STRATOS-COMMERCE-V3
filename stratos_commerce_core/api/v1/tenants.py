from fastapi import APIRouter, Depends, Header, HTTPException, Request, status

from stratos_commerce_core.auth.jwt_auth import verify_token
from stratos_commerce_core.pipeline.schemas import MerchantCreateRequest

router = APIRouter(prefix="/tenants", tags=["tenants"])


async def get_current_user(authorization: str | None = Header(default=None)) -> dict:
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")
    token = authorization.replace("Bearer ", "", 1)
    payload = verify_token(token)
    return payload


@router.post("/register")
def register_tenant(payload: MerchantCreateRequest, request: Request, user: dict = Depends(get_current_user)) -> dict:
    if user.get("role") not in {"super_admin", "merchant_admin"}:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient role")
    tenant_id = getattr(request.state, "tenant_id", payload.tenant_id)
    return {
        "status": "tenant_registered",
        "tenant_id": tenant_id,
        "subdomain": payload.subdomain,
        "legal_name": payload.legal_name,
    }
