import os
from typing import Any, Dict

import stripe

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_placeholder")


class MultiVendorEscrowGateway:
    """Coordinates multi-vendor escrow split payouts using Stripe Connect."""

    @staticmethod
    async def create_split_checkout_session(
        order_total: int,
        merchant_account_id: str,
        platform_fee_cents: int,
    ) -> Dict[str, Any]:
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "product_data": {
                                "name": "B2B Enterprise Batch Order Checkout"
                            },
                            "unit_amount": order_total,
                        },
                        "quantity": 1,
                    }
                ],
                payment_intent_data={
                    "application_fee_amount": platform_fee_cents,
                    "transfer_data": {"destination": merchant_account_id},
                },
                mode="payment",
                success_url="https://stratos-commerce.com/success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url="https://stratos-commerce.com/cancel",
            )
            return {"checkout_url": session.url, "session_id": session.id}
        except stripe.error.StripeError as exc:  # type: ignore[attr-defined]
            return {"error": f"Stripe transaction routing crashed: {exc}"}
