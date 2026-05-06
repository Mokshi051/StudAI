import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import joblib
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# -----------------------------
# Load dataset
# -----------------------------
data = pd.read_csv("../../synthetic_student_burnout_dataset (1).csv")

X = data.drop(columns=[
    "student_id",
    "week",
    "year",
    "burnout_status",
    "burnout_severity"
])
y_status = data["burnout_status"]
y_severity = data["burnout_severity"]

# -----------------------------
# Load trained models
# -----------------------------
status_model = joblib.load("burnout_status_model.pkl")
severity_model = joblib.load("burnout_severity_model.pkl")
severity_encoder = joblib.load("severity_encoder.pkl")

# -----------------------------
# Predictions
# -----------------------------
y_status_pred = status_model.predict(X)
y_severity_pred_encoded = severity_model.predict(X)
y_severity_pred = severity_encoder.inverse_transform(y_severity_pred_encoded)

# -----------------------------
# Evaluation - Burnout Status
# -----------------------------
print("\n==== Burnout Status Model ====")
print("Accuracy:", accuracy_score(y_status, y_status_pred))
print("Precision:", precision_score(y_status, y_status_pred))
print("Recall:", recall_score(y_status, y_status_pred))
print("F1 Score:", f1_score(y_status, y_status_pred))
print("Confusion Matrix:\n", confusion_matrix(y_status, y_status_pred))

# -----------------------------
# Evaluation - Burnout Severity
# -----------------------------
print("\n==== Burnout Severity Model ====")
print("Accuracy:", accuracy_score(y_severity, y_severity_pred))
print("Precision (macro):", precision_score(y_severity, y_severity_pred, average="macro"))
print("Recall (macro):", recall_score(y_severity, y_severity_pred, average="macro"))
print("Confusion Matrix:\n", confusion_matrix(y_severity, y_severity_pred))

print("\nClassification Report:\n")
print(classification_report(y_severity, y_severity_pred))

# -----------------------------
# Confusion Matrix Visualization
# -----------------------------

cm = confusion_matrix(y_severity, y_severity_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    cbar=True,
    square=True,
    linewidths=0.5
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Burnout Severity Confusion Matrix")

plt.tight_layout()
plt.savefig("burnout_severity_confusion_matrix.png", dpi=300)
plt.show()

# -----------------------------
# Accuracy vs Precision Plot
# -----------------------------

accuracy = accuracy_score(y_severity, y_severity_pred)
precision = precision_score(y_severity, y_severity_pred, average="macro")

metrics = ["Accuracy", "Precision"]
scores = [accuracy, precision]

plt.figure(figsize=(6, 4))
plt.plot(metrics, scores, marker="o")
plt.ylim(0.9, 1.0)
plt.xlabel("Metrics")
plt.ylabel("Score")
plt.title("Burnout Severity: Accuracy vs Precision")
plt.grid(True)

plt.tight_layout()
plt.savefig("accuracy_vs_precision.png", dpi=300)
plt.show()