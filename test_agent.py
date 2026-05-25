from src.inference.predictor import (
    predict_risk
)

from src.explainability.explainer import (
    explain_prediction
)

from src.rag.retriever import (
    retrieve_rules
)

from src.agent.recommend import (
    recommend_offer
)


sample = {
    "time_spent_sec": 18,
    "page_stage": "checkout",
    "device_type": "android",
    "delivery_zone": "metro",
    "cart_value": 0,
    "cart_items_count": 0,
    "delivery_eta_days": 2,
    "coupon_status": "none",
    "is_returning_user": 0,
    "idle_seconds": 10,
}

risk = predict_risk(sample)

reasons = explain_prediction(
    sample
)

rules = retrieve_rules(
    reasons,
    sample["page_stage"]
)

offer = recommend_offer(
    risk["risk_score"],
    reasons,
    rules,
    sample,
)

print(
    "Risk:",
    risk
)

print(
    "Reasons:",
    reasons
)

print(
    "Offer:",
    offer
)