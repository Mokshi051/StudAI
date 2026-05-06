# Smart Study Planner & Burnout Detector

## Project Structure
- `backend/api/` — Flask REST API (app.py)
- `backend/core/` — Business logic (models, schemas, timetable, wellness)
- `backend/ml/` — ML training & evaluation scripts
- `backend/notifications/` — Desktop notification service
- `backend/tests/` — API test scripts
- `data/models/` — Trained .pkl model files (gitignored)
- `data/` — Dataset CSV
- `frontend/pages/` — HTML pages
- `frontend/assets/` — Images, CSS

## Running the Backend
```bash
pip install -r requirements.txt
cd backend/api
python app.py
```

## Running Notifications
```bash
cd backend/notifications
python notification_service.py
```
