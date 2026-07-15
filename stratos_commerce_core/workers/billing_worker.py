from celery import shared_task


@shared_task
def generate_invoice_pdf(order_id: str, merchant_id: int) -> dict:
    """Placeholder async invoice generation pipeline."""
    return {
        "order_id": order_id,
        "merchant_id": merchant_id,
        "status": "invoice_generated",
        "document_path": f"/tmp/{order_id}.pdf",
    }
