import csv
import os
from datetime import datetime

FILE = "data.csv"

def init_csv():
    if not os.path.exists(FILE):
        with open(FILE, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp", "worker_id", "heart_rate", "body_temp",
                "gas", "ambient_temp", "humidity", "motion", "risk"
            ])

def save_to_csv(data):
    with open(FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(),
            data["worker_id"],
            data["heart_rate"],
            data["body_temp"],
            data["gas"],
            data["ambient_temp"],
            data["humidity"],
            data["motion"],
            data["risk"]
        ])