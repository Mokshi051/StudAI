import os
import sys

# Walk up to project root (ssp/) so all backend.* imports resolve
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from backend.core.wellness_recommender import get_wellness_recommendations
from backend.core.schemas import BurnoutPredictionSchema
from backend.core.models import predict_burnout
from backend.core.database import init_db, save_prediction
from backend.core.timetable_generator import generate_timetable
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
init_db()

burnout_schema = BurnoutPredictionSchema()

# -------------------------------------------------
# Burnout Prediction API
# -------------------------------------------------
@app.route("/predict_burnout", methods=["POST"])
def predict_burnout_route():

    data = request.json

    errors = burnout_schema.validate(data)
    if errors:
        return jsonify({"errors": errors}), 400

    features = [
        data["current_cgpa"],
        data["assignment_score"],
        data["attendance_rate"],
        data["assignments_on_time"],
        data["assignments_late"],
        data["assignments_missing"],
        data["hours_before_deadline"],
        data["lms_logins"],
        data["days_since_last_lms_login"],
        data["library_visits"],
        data["library_study_hours"],
        data["campus_activities"],
        data["peer_interactions"],
        data["stress_level"],
        data["sleep_hours"],
        data["sleep_quality"]
    ]

    result = predict_burnout(features)
    return jsonify(result)


# -------------------------------------------------
# Timetable Generation API
# -------------------------------------------------
@app.route("/generate_timetable", methods=["POST"])
def generate_timetable_route():

    data = request.json

    weekly_hours = data["weekly_availability"]
    burnout_status = data["burnout_status"]
    burnout_severity = data["burnout_severity"]
    lighten_workload = data.get("lighten_workload", False)
    regenerate = data.get("regenerate", False)

    class Profile:
        def __init__(self, weekly_availability):
            self.weekly_availability = weekly_availability

    profile = Profile(weekly_hours)

    timetable = generate_timetable(
        profile,
        burnout_status,
        burnout_severity,
        lighten_workload,
        regenerate
    )

    return jsonify(timetable)


# -------------------------------------------------
# Wellness Recommendations API
# -------------------------------------------------
@app.route("/wellness_recommendations", methods=["POST"])
def wellness_recommendations_route():

    data = request.json

    burnout_status = data["burnout_status"]
    burnout_severity = data["burnout_severity"]

    recommendations = get_wellness_recommendations(
        burnout_status,
        burnout_severity
    )

    return jsonify(recommendations)


# -------------------------------------------------
# Health Check
# -------------------------------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Smart Study Planner Backend Running"})


# -------------------------------------------------
# Run Server
# -------------------------------------------------
if __name__ == "__main__":
    print("REGISTERED ROUTES:")
    print(app.url_map)
    app.run(debug=True)
