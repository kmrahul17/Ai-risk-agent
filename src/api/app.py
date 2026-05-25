from fastapi import FastAPI
from fastapi.middleware.cors import (
    CORSMiddleware
)

from src.inference.predictor import (
    predict_risk,
)

from src.explainability.explainer import (
    explain_prediction,
)

from src.rag.retriever import (
    retrieve_rules,
)

from src.agent.recommend import (
    recommend_offer,
)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "status":
        "Risk Agent API running"
    }


@app.post("/analyze")
def analyze(session: dict):

    risk = predict_risk(
        session
    )

    reasons = explain_prediction(
        session
    )

    rules = retrieve_rules(
        reasons,
        session["page_stage"],
    )

    offer = recommend_offer(
        risk["risk_score"],
        reasons,
        rules,
        session,
    )

    return {
        "risk": risk,
        "reasons": reasons,
        "offer": offer,
    }