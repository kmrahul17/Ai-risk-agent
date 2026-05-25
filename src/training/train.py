import joblib

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

from configs.settings import *
from configs.features import *

from src.preprocessing.encoder import encode_dataframe


def train_model(df):
    df = encode_dataframe(df)

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=TEST_SIZE,
            random_state=RANDOM_SEED,
        )
    )

    model = XGBClassifier(
    n_estimators=150,
    max_depth=4,
    learning_rate=0.08,
    subsample=0.9,
    colsample_bytree=0.9,
    objective="binary:logistic",
    eval_metric="logloss",
    random_state=RANDOM_SEED,
)

    model.fit(
        X_train,
        y_train
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    return model, X_test, y_test