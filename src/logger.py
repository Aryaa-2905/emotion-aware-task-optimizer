import csv
from datetime import datetime

def log_emotion(employee_id, emotion, source, action):
    with open("emotion_logs.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(),
            employee_id,
            source,
            emotion,
            action
        ])
