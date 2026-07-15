import os
from celery import Celery

broker_url = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/1")
result_backend = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/2")

app = Celery(
    "stratos_commerce",
    broker=broker_url,
    backend=result_backend,
    include=["stratos_commerce_core.workers.order_worker", "stratos_commerce_core.workers.billing_worker"],
)

app.conf.update(task_serializer="json", accept_content=["json"], result_serializer="json")
