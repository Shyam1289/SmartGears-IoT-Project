from fastapi import APIRouter
import pandas as pd
from app.services.simulator import generate_worker_data
from app.services.ai_engine import ai_decision
from app.services.csv_service import save_to_csv, init_csv

router = APIRouter()

init_csv()

@router.get("/worker/{worker_id}")
def get_worker(worker_id: int):
    data = generate_worker_data(worker_id)
    data["risk"] = ai_decision(data)

    save_to_csv(data)

    # read history from csv
    df = pd.read_csv("data.csv")
    history = df[df["worker_id"] == worker_id].tail(30).to_dict(orient="records")

    return {
        "current": data,
        "history": history
    }