import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

# ---------------------------
# Load Dataset
# ---------------------------
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.abspath(
    os.path.join(BASE_DIR, "..", "..", "data",
                 "synthetic_student_burnout_dataset (1).csv")
)

print(csv_path)

data = pd.read_csv(csv_path)

# ---------------------------
# Feature Columns
# ---------------------------
FEATURES = [
    "current_cgpa",
    "assignment_score",
    "attendance_rate",
    "assignments_on_time",
    "assignments_late",
    "assignments_missing",
    "hours_before_deadline",
    "lms_logins",
    "days_since_last_lms_login",
    "library_visits",
    "library_study_hours",
    "campus_activities",
    "peer_interactions",
    "stress_level",
    "sleep_hours",
    "sleep_quality"
]

X = data[FEATURES]

# =====================================================
# MODEL 1: Burnout Status (Yes / No)
# =====================================================
y_status = data["burnout_status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y_status, test_size=0.2, random_state=42
)

burnout_status_model = RandomForestClassifier(
    n_estimators=150,
    random_state=42
)

burnout_status_model.fit(X_train, y_train)

joblib.dump(burnout_status_model, "burnout_status_model.pkl")

# =====================================================
# MODEL 2: Burnout Severity (Low / Moderate / High)
# =====================================================
severity_encoder = LabelEncoder()
y_severity = severity_encoder.fit_transform(data["burnout_severity"])

X_train, X_test, y_train, y_test = train_test_split(
    X, y_severity, test_size=0.2, random_state=42
)

burnout_severity_model = RandomForestClassifier(
    n_estimators=150,
    random_state=42
)

burnout_severity_model.fit(X_train, y_train)

joblib.dump(burnout_severity_model, "burnout_severity_model.pkl")
joblib.dump(severity_encoder, "severity_encoder.pkl")

print("✅ Models trained and saved successfully")