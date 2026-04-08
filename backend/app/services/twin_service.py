from app.models.database import SessionLocal
from app.models.models import SensorData

def store_data(data):
    db = SessionLocal()

    record = SensorData(**data)
    db.add(record)
    db.commit()
    db.close()


def get_worker_history(worker_id):
    db = SessionLocal()

    records = db.query(SensorData)\
        .filter(SensorData.worker_id == worker_id)\
        .order_by(SensorData.timestamp.desc())\
        .limit(30)\
        .all()

    db.close()

    return [r.__dict__ for r in records]