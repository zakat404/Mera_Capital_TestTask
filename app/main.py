import uvicorn
from fastapi import FastAPI
from app.api.routes.currency import router as currency_router
from app.models.currency_models import Base
from app.db.database import engine

app = FastAPI()


app.include_router(currency_router, prefix="/api")

# Создание таблиц
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
