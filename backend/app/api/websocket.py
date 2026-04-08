from fastapi import APIRouter, WebSocket
import asyncio
from app.services.simulator import generate_worker_data
from app.services.ai_engine import ai_decision
from app.services.csv_service import save_to_csv

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()

    while True:
        workers = []

        for i in range(1, 4):
            data = generate_worker_data(i)
            data["risk"] = ai_decision(data)

            save_to_csv(data)

            workers.append(data)

        await ws.send_json(workers)
        await asyncio.sleep(2)