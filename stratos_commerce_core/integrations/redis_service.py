import os
from typing import Any, Dict, List

import redis


class RedisService:
    def __init__(self) -> None:
        self.client = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"))

    def ping(self) -> Dict[str, Any]:
        try:
            return {"status": "ok", "pong": self.client.ping()}
        except Exception as exc:  # pragma: no cover - defensive fallback
            return {"status": "error", "detail": str(exc)}

    def list_inventory_events(self) -> List[Dict[str, Any]]:
        return [
            {"channel": "inventory", "event": "stock_updated", "sku": "SKU-1001", "quantity": 42},
            {"channel": "inventory", "event": "reservation_created", "sku": "SKU-1002", "quantity": 19},
        ]
