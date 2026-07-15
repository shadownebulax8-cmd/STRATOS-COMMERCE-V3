from celery import shared_task


@shared_task
def process_inventory_reservation(product_id: int, quantity: int) -> dict:
    """Simulates background inventory reservation for an order."""
    return {
        "product_id": product_id,
        "reserved_quantity": quantity,
        "status": "reserved",
    }
