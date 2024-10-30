# app/main.py

from fastapi import FastAPI
from app.api.routes.currency import router as currency_router
from app.clients.deribit_client import DeribitClient
from app.db.database import init_db
import asyncio

app = FastAPI(title="Deribit Client API")

app.include_router(currency_router, prefix="/api/v1")

# Запуск клиента для получения данных каждые 60 секунд
deribit_client = DeribitClient()

@app.on_event("startup")
async def startup_event():
    await init_db()  # Инициализация базы данных
    asyncio.create_task(deribit_client.start_fetching())
