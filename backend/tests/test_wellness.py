import requests

url = "http://127.0.0.1:5000/wellness_recommendations"

payload = {
    "burnout_status": "At Risk",
    "burnout_severity": "High"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response Text:", response.text)

# Only parse JSON if response is OK
if response.status_code == 200:
    print("Parsed JSON:", response.json())