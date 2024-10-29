from fastapi import APIRouter, HTTPException
from app.services.currency_service import CurrencyService

router = APIRouter()

@router.get("/prices")
async def get_all_prices(ticker: str):
    prices = await CurrencyService.get_all_prices(ticker)
    if not prices:
        raise HTTPException(status_code=404, detail="Currency not found")
    return prices

@router.get("/latest_price")
async def get_latest_price(ticker: str):
    price = await CurrencyService.get_latest_price(ticker)
    if not price:
        raise HTTPException(status_code=404, detail="Currency not found")
    return price

@router.get("/prices_in_range")
async def get_prices_in_range(ticker: str, start_date: int, end_date: int):
    prices = await CurrencyService.get_prices_within_date_range(ticker, start_date, end_date)
    if not prices:
        raise HTTPException(status_code=404, detail="No data found for the given date range")
    return prices
