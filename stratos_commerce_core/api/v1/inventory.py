from fastapi import APIRouter, Depends, Header, HTTPException, Request, status
from pydantic import BaseModel

from stratos_commerce_core.auth.jwt_auth import verify_token
from stratos_commerce_core.pipeline.schemas import InventorySnapshot

router = APIRouter(prefix="/inventory", tags=["inventory"])


class InventoryEventPayload(BaseModel):
    product_id: int
    available_stock: int


async def get_current_user(authorization: str | None = Header(default=None)) -> dict:
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")
    token = authorization.replace("Bearer ", "", 1)
    payload = verify_token(token)
    return payload


@router.get("/snapshot", response_model=InventorySnapshot)
def inventory_snapshot(request: Request, user: dict = Depends(get_current_user)) -> InventorySnapshot:
    tenant_id = getattr(request.state, "tenant_id", "alpha")
    return InventorySnapshot(product_id=1, available_stock=42, updated_at=tenant_id)


@router.post("/emit")
def emit_inventory_event(payload: InventoryEventPayload, user: dict = Depends(get_current_user)) -> dict:
    if user.get("role") not in {"merchant_admin", "operations"}:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient role")
    return {"status": "event_queued", "product_id": payload.product_id, "available_stock": payload.available_stock}
