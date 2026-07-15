from fastapi import APIRouter, Depends, Header, HTTPException, status

from stratos_commerce_core.auth.jwt_auth import verify_token
from stratos_commerce_core.integrations.postgres_service import PostgresService
from stratos_commerce_core.integrations.redis_service import RedisService

router = APIRouter(prefix="/analytics", tags=["analytics"])


async def get_current_user(authorization: str | None = Header(default=None)) -> dict:
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")
    token = authorization.replace("Bearer ", "", 1)
    payload = verify_token(token)
    return payload


@router.get("/overview")
def analytics_overview(user: dict = Depends(get_current_user)) -> dict:
    if user.get("role") not in {"super_admin", "merchant_admin"}:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient role")

    postgres = PostgresService()
    redis = RedisService()
    return {
        "postgres": postgres.health(),
        "redis": redis.ping(),
        "metrics": postgres.list_metrics(),
        "inventory_events": redis.list_inventory_events(),
    }
