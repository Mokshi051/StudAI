import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "../../data/models")

burnout_status_model = joblib.load(
    os.path.join(MODELS_DIR, "burnout_status_model.pkl")
)

burnout_severity_model = joblib.load(
    os.path.join(MODELS_DIR, "burnout_severity_model.pkl")
)


def predict_burnout(features):

    status_pred = burnout_status_model.predict([features])[0]
    severity_pred = burnout_severity_model.predict([features])[0]

    status_map = {
        0: "Low Risk",
        1: "At Risk"
    }

    severity_map = {
        1: "Very Low",
        2: "Low",
        3: "Moderate",
        4: "High",
        5: "Severe"
    }

    return {
        "burnout_status": status_map.get(int(status_pred), "Unknown"),
        "burnout_severity": severity_map.get(int(severity_pred), "Unknown")
    }