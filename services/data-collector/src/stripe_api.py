import os
import stripe

def fetch_stripe_data():
    stripe.api_key = os.getenv("STRIPE_API_KEY")
    charges = stripe.Charge.list(limit=10)
    data = []
    for c in charges.data:
        data.append({
            "id": c.id,
            "amount": c.amount,
            "created": c.created,
            "status": c.status
        })
    return data