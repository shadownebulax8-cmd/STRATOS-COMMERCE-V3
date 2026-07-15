from fastapi import APIRouter
from fastapi.websockets import WebSocket, WebSocketDisconnect

router = APIRouter(prefix="/ws", tags=["ws"])


@router.websocket("/inventory")
async def inventory_websocket(websocket: WebSocket) -> None:
    await websocket.accept()
    try:
        while True:
            await websocket.send_json(
                {
                    "event": "inventory_update",
                    "sku": "SKU-1001",
                    "available_stock": 42,
                    "timestamp": "live",
                }
            )
            await websocket.receive_text()
    except WebSocketDisconnect:
        return
