from fastapi import APIRouter, Depends, Header, HTTPException, status

from stratos_commerce_core.auth.jwt_auth import verify_token
from stratos_commerce_core.core.stripe_gateway import MultiVendorEscrowGateway
from stratos_commerce_core.pipeline.schemas import OrderPlacementRequest

router = APIRouter(prefix="/orders", tags=["orders"])


async def get_current_user(authorization: str | None = Header(default=None)) -> dict:
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")
    token = authorization.replace("Bearer ", "", 1)
    payload = verify_token(token)
    return payload


@router.post("/place")
async def place_order(payload: OrderPlacementRequest, user: dict = Depends(get_current_user)) -> dict:
    if user.get("role") not in {"merchant_admin", "sales_ops"}:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient role")

    checkout = await MultiVendorEscrowGateway.create_split_checkout_session(
        order_total=payload.quantity * 1000,
        merchant_account_id="acct_merchant_demo",
        platform_fee_cents=250,
    )
    return {"status": "checkout_created", **checkout}
