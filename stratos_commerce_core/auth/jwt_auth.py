import base64
import hashlib
import hmac
import json
import os
from datetime import datetime, timedelta, timezone
from typing import Any, Dict

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "stratos-dev-secret")


def _b64encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("utf-8").rstrip("=")


def _b64decode(data: str) -> bytes:
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


def create_access_token(sub: str, role: str, tenant_id: str, expires_minutes: int = 60) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": sub,
        "role": role,
        "tenant_id": tenant_id,
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=expires_minutes)).timestamp()),
    }
    header = {"alg": "HS256", "typ": "JWT"}
    encoded_header = _b64encode(json.dumps(header, separators=(",", ":")).encode("utf-8"))
    encoded_payload = _b64encode(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    signing_input = f"{encoded_header}.{encoded_payload}".encode("utf-8")
    signature = hmac.new(SECRET_KEY.encode("utf-8"), signing_input, hashlib.sha256).digest()
    return f"{encoded_header}.{encoded_payload}.{_b64encode(signature)}"


def verify_token(token: str) -> Dict[str, Any]:
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("Invalid token format")
    header_b64, payload_b64, signature_b64 = parts
    signing_input = f"{header_b64}.{payload_b64}".encode("utf-8")
    expected_signature = _b64encode(
        hmac.new(SECRET_KEY.encode("utf-8"), signing_input, hashlib.sha256).digest()
    )
    if not hmac.compare_digest(signature_b64, expected_signature):
        raise ValueError("Invalid token signature")
    payload = json.loads(_b64decode(payload_b64).decode("utf-8"))
    if int(payload["exp"]) < int(datetime.now(timezone.utc).timestamp()):
        raise ValueError("Token expired")
    return payload
