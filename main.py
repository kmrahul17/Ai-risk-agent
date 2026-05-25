from src.data_generation.generator import (
    generate_dataset,
)

from src.training.train import (
    train_model,
)

from src.training.evaluate import (
    evaluate_model,
)


def main():
    df = generate_dataset()
    
    print(df["abandoned"].value_counts(normalize=True))
    
    model, X_test, y_test = (
        train_model(df)
    )

    evaluate_model(
        model,
        X_test,
        y_test,
    )


if __name__ == "__main__":
    main()