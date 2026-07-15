import os
from typing import Any, Dict, List

from sqlalchemy import create_engine, text


class PostgresService:
    def __init__(self) -> None:
        self.database_url = os.getenv("DATABASE_BASE_URL", "postgresql://postgres:postgres@localhost:5432/stratos")
        self.engine = create_engine(self.database_url)

    def health(self) -> Dict[str, Any]:
        with self.engine.connect() as connection:
            result = connection.execute(text("SELECT 1 AS ok"))
            row = result.fetchone()
            return {"status": "ok", "result": row[0] if row else None}

    def list_metrics(self) -> List[Dict[str, Any]]:
        return [
            {"name": "orders", "value": 128},
            {"name": "revenue", "value": 8420},
            {"name": "tenants", "value": 3},
        ]
