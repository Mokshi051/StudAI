import sqlite3
from datetime import datetime

DB_NAME = "smart_study_planner.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            study_hours REAL,
            sleep_hours REAL,
            stress_level REAL,
            burnout_status TEXT,
            burnout_severity TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_prediction(name, study_hours, sleep_hours, stress_level,
                    burnout_status, burnout_severity):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions
        (name, study_hours, sleep_hours, stress_level,
         burnout_status, burnout_severity, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        study_hours,
        sleep_hours,
        stress_level,
        burnout_status,
        burnout_severity,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()