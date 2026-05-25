import joblib

from sklearn.preprocessing import (
    LabelEncoder,
)

from configs.settings import (
    ENCODER_PATH,
    PROCESSED_DATA_PATH,
)


def encode_dataframe(df):
    encoders = {}

    categorical = [
        "page_stage",
        "device_type",
        "delivery_zone",
        "coupon_status",
    ]

    for col in categorical:
        encoder = LabelEncoder()

        df[col] = encoder.fit_transform(
            df[col]
        )

        encoders[col] = encoder

    joblib.dump(
        encoders,
        ENCODER_PATH
    )

    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )

    return df