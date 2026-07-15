from fastapi import APIRouter, Depends, Header, HTTPException, status

from stratos_commerce_core.auth.jwt_auth import verify_token

router = APIRouter(prefix="/admin", tags=["admin"])


async def get_current_user(authorization: str | None = Header(default=None)) -> dict:
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")
    token = authorization.replace("Bearer ", "", 1)
    payload = verify_token(token)
    return payload


@router.get("/overview")
def admin_overview(user: dict = Depends(get_current_user)) -> dict:
    if user.get("role") != "super_admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient role")
    return {
        "status": "ok",
        "mode": "multi_tenant_b2b_marketplace",
        "tenants": ["alpha", "beta", "gamma"],
        "features": ["escrow", "inventory_stream", "split_checkout"],
    }
