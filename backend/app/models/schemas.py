from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.models.database import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer)
    heart_rate = Column(Integer)
    body_temp = Column(Float)
    gas = Column(Integer)
    ambient_temp = Column(Float)
    humidity = Column(Integer)
    motion = Column(String)
    risk = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)