from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from stratos_commerce_core.auth.jwt_auth import create_access_token, verify_token

router = APIRouter(prefix="/auth", tags=["auth"])


class TokenRequest(BaseModel):
    sub: str
    role: str = "merchant_admin"
    tenant_id: str = "alpha"


@router.post("/token")
def issue_token(payload: TokenRequest) -> dict:
    token = create_access_token(sub=payload.sub, role=payload.role, tenant_id=payload.tenant_id)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/verify")
def verify_token_endpoint(token: str) -> dict:
    try:
        payload = verify_token(token)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    return {"valid": True, "payload": payload}
