
from fastapi import FastAPI
from app.api.routes.currency import router as currency_router
from app.clients.deribit_client import DeribitClient
from app.db.database import init_db
import asyncio
import logging
from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

deribit_client = DeribitClient()


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await init_db()
        logger.info("Database initialized successfully.")

        fetch_task = asyncio.create_task(deribit_client.start_fetching())

        yield

    except Exception as e:
        logger.exception(f"Exception occurred during lifespan: {e}")
    finally:
        deribit_client.stop_fetching()
        await fetch_task


app = FastAPI(
    title="Deribit Client API",
    description="API для получения данных о курсах валют с биржи Deribit. Включает методы для получения всех данных, последней цены, а также данных в пределах заданных дат.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(currency_router, prefix="/api")


@app.get("/")
async def read_root():
    return {"message": "API is up and running!"}
