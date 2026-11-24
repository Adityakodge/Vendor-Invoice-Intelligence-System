
import joblib
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR
    / " freight_cost_prediction"
    / "models"
    / "predict_freight_model.pkl"
)


def load_model(model_path=MODEL_PATH):

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found: {model_path}"
        )

    model = joblib.load(model_path)

    print("Model loaded successfully!")

    return model


def predict_freight_cost(input_data):
    """
    Predict freight cost for new vendor invoices.

    Parameters
    ----------
    input_data : dict
        Input features for freight cost prediction.

    Returns
    -------
    pd.DataFrame
        DataFrame with predicted freight cost.
    """

    # Load trained model
    model = load_model()

    # Convert input data into DataFrame
    input_df = pd.DataFrame(input_data)

    # Make predictions
    predictions = model.predict(input_df)

    # Add predicted freight column
    input_df["Predicted_Freight"] = predictions.round(2)

    return input_df


if __name__ == "__main__":

    # Example inference run (local testing)

    sample_data = {
        "Dollars": [18500, 9000, 3000, 200]
    }

    prediction = predict_freight_cost(sample_data)

    print("\nFreight Cost Prediction:")
    print(prediction)
