from src.explainability.explainer import (
    explain_prediction
)

sample = {
    "time_spent_sec": 52,
    "page_stage": "cart",
    "device_type": "android",
    "delivery_zone": "remote",
    "cart_value": 1800,
    "cart_items_count": 2,
    "delivery_eta_days": 4,
    "coupon_status": "available",
    "is_returning_user": 0,
    "idle_seconds": 18,
}

print(
    explain_prediction(sample)
)