from typing import Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class TenantContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> object:
        request.state.tenant_id = request.headers.get("x-tenant-id", "alpha")
        return await call_next(request)
