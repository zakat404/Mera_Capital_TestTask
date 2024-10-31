# app/api/routes/currency.py

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.services.currency_service import CurrencyService
from app.models.currency_models import CurrencyData

router = APIRouter()
service = CurrencyService()


@router.get("v1/currency", response_model=List[CurrencyData])
async def get_all_data(ticker: str = Query(...)):
    data = await service.get_all_data(ticker)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data


@router.get("/currency/latest", response_model=CurrencyData)
async def get_latest_price(ticker: str = Query(...)):
    data = await service.get_latest_price(ticker)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data


@router.get("/currency/filter", response_model=List[CurrencyData])
async def get_data_by_date(
    ticker: str = Query(...), start_date: int = Query(...), end_date: int = Query(...)
):
    data = await service.get_data_by_date(ticker, start_date, end_date)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data
