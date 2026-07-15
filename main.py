from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from stratos_commerce_core.api.middleware import TenantContextMiddleware
from stratos_commerce_core.api.v1.admin import router as admin_router
from stratos_commerce_core.api.v1.auth import router as auth_router
from stratos_commerce_core.api.v1.inventory import router as inventory_router
from stratos_commerce_core.api.v1.orders import router as orders_router
from stratos_commerce_core.api.v1.tenants import router as tenants_router
from stratos_commerce_core.config.settings import settings
from stratos_commerce_core.startup import startup_banner
from stratos_commerce_core.streaming.inventory_stream import InventoryStreamClient

app = FastAPI(title=settings.project_name, version="3.0.0")
app.add_middleware(TenantContextMiddleware)
app.include_router(auth_router, prefix="/api/v1")
app.include_router(inventory_router, prefix="/api/v1")
app.include_router(orders_router, prefix="/api/v1")
app.include_router(tenants_router, prefix="/api/v1")
app.include_router(admin_router, prefix="/api/v1")


@app.get("/")
def healthcheck() -> dict:
    return {
        "service": settings.project_name,
        "environment": settings.environment,
        "status": "operational",
        "features": ["auth", "inventory", "orders", "tenants", "admin"],
    }


@app.get("/health")
def detailed_healthcheck() -> dict:
    return {
        "status": "healthy",
        "service": settings.project_name,
        "environment": settings.environment,
        "redis": settings.redis_url,
        "database": settings.database_base_url,
    }


@app.get("/startup")
def startup_info() -> dict:
    return startup_banner()


@app.get("/api/v1/stream/inventory")
def stream_inventory() -> StreamingResponse:
    client = InventoryStreamClient()

    def event_stream():
        yield "data: {\"status\":\"connected\",\"channel\":\"inventory\"}\n\n"
        client.publish("inventory", {"event": "connected"})

    return StreamingResponse(event_stream(), media_type="text/event-stream")
