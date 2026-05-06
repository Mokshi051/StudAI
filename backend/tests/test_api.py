import requests

url = "http://127.0.0.1:5000/predict_burnout"

data = {
    "current_cgpa": 8.5,
    "assignment_score": 75,
    "attendance_rate": 85,
    "assignments_on_time": 8,
    "assignments_late": 1,
    "assignments_missing": 0,
    "hours_before_deadline": 5,
    "lms_logins": 20,
    "days_since_last_lms_login": 1,
    "library_visits": 3,
    "library_study_hours": 6,
    "campus_activities": 2,
    "peer_interactions": 5,
    "stress_level": 6,
    "sleep_hours": 6,
    "sleep_quality": 7
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())