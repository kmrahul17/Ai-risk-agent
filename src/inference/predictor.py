import joblib
import pandas as pd

from configs.features import FEATURE_COLUMNS
from configs.settings import (
    MODEL_PATH,
    ENCODER_PATH,
)


model = joblib.load(MODEL_PATH)

encoders = joblib.load(
    ENCODER_PATH
)


def encode_input(data):
    row = data.copy()

    categorical = [
        "page_stage",
        "device_type",
        "delivery_zone",
        "coupon_status",
    ]

    for col in categorical:
        row[col] = (
            encoders[col]
            .transform([row[col]])[0]
        )

    return row


def predict_risk(data):
    row = encode_input(data)

    df = pd.DataFrame([row])

    prob = model.predict_proba(
        df[FEATURE_COLUMNS]
    )[0][1]

    return {
        "risk_score": round(
            float(prob), 3
        )
    }