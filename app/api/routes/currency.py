from fastapi import APIRouter, HTTPException, Query
from typing import List
from datetime import datetime
from app.services.currency_service import CurrencyService
from app.models.currency_models import CurrencyData
import pytz

router = APIRouter()
service = CurrencyService()

@router.get("/currency", response_model=List[CurrencyData], summary="Get All Data", description="Получение всех сохраненных данных по указанной валюте.")
async def get_all_data(ticker: str = Query(..., description="Ticker валюты, например 'btc_usd' или 'eth_usd'")):
    data = await service.get_all_data(ticker)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.get("/currency/latest", response_model=CurrencyData, summary="Get Latest Price", description="Получение последней сохраненной цены по указанной валюте.")
async def get_latest_price(ticker: str = Query(..., description="Ticker валюты, например 'btc_usd' или 'eth_usd'")):
    data = await service.get_latest_price(ticker)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.get("/currency/filter", response_model=List[CurrencyData], summary="Get Data By Date", description="Получение сохраненных данных по указанной валюте в пределах заданных дат.")
async def get_data_by_date(
    ticker: str = Query(..., description="Ticker валюты, например 'btc_usd' или 'eth_usd'"),
    start_date: datetime = Query(..., description="Начальная дата в формате ISO, например '2024-10-30T00:00:00'"),
    end_date: datetime = Query(..., description="Конечная дата в формате ISO, например '2024-10-31T23:59:59'")
):
    data = await service.get_all_data(ticker)

    local_tz = pytz.timezone('Europe/Moscow')
    start_date = local_tz.localize(start_date).astimezone(pytz.UTC)
    end_date = local_tz.localize(end_date).astimezone(pytz.UTC)

    filtered_data = [
        record for record in data
        if start_date <= record.timestamp <= end_date
    ]

    if not filtered_data:
        raise HTTPException(status_code=404, detail="Data not found")
    return filtered_data