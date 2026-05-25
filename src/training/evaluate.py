from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
)


def evaluate_model(
    model,
    X_test,
    y_test,
):
    preds = model.predict(X_test)

    probs = model.predict_proba(
        X_test
    )[:, 1]

    print(
        "Accuracy:",
        accuracy_score(
            y_test,
            preds
        )
    )

    print(
        "ROC AUC:",
        roc_auc_score(
            y_test,
            probs
        )
    )