import os
from typing import Any, Dict

import redis


class InventoryStreamClient:
    def __init__(self, redis_url: str | None = None) -> None:
        self.client = redis.from_url(redis_url or os.getenv("REDIS_URL", "redis://localhost:6379/0"))

    def publish(self, channel: str, payload: Dict[str, Any]) -> None:
        self.client.publish(channel, str(payload))

    def subscribe(self, channel: str) -> Any:
        pubsub = self.client.pubsub()
        pubsub.subscribe(channel)
        return pubsub
