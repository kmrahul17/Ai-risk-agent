import joblib
import pandas as pd
import xgboost as xgb

from configs.features import (
    FEATURE_COLUMNS,
)

from configs.settings import (
    MODEL_PATH,
    ENCODER_PATH,
)


model = joblib.load(
    MODEL_PATH
)

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


def explain_prediction(data):
    row = encode_input(data)

    df = pd.DataFrame([row])

    dmatrix = xgb.DMatrix(
        df[FEATURE_COLUMNS]
    )

    booster = model.get_booster()

    contribs = booster.predict(
        dmatrix,
        pred_contribs=True
    )[0]

    # last column is bias
    values = contribs[:-1]

    pairs = list(
        zip(
            FEATURE_COLUMNS,
            values
        )
    )

    pairs.sort(
        key=lambda x: abs(x[1]),
        reverse=True
    )

    top = pairs[:3]

    return {
        feature: round(
            float(score),
            3
        )
        for feature, score in top
    }