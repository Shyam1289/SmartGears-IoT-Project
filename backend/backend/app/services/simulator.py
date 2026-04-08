import random

def generate_worker_data(worker_id: int):
    return {
        "worker_id": worker_id,
        "heart_rate": random.randint(60, 130),
        "body_temp": round(36 + random.random() * 2, 1),
        "gas": random.randint(100, 500),
        "ambient_temp": round(25 + random.random() * 10, 1),
        "humidity": random.randint(40, 80),
        "motion": "Normal" if random.random() > 0.1 else "Fall Detected"
    }