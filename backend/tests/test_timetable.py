import requests

url = "http://127.0.0.1:5000/generate_timetable"

data = {
    "weekly_availability": 40,
    "burnout_status": "At Risk",
    "burnout_severity": "Severe",
    "lighten_workload": True,
    "regenerate": False
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())