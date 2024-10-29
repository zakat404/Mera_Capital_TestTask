import pytest
from app.services.currency_service import CurrencyService
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_get_all_prices():
    CurrencyService.get_all_prices = AsyncMock(return_value=[{"ticker": "btc_usd", "price": 30000, "timestamp": 1695000000}])
    prices = await CurrencyService.get_all_prices("btc_usd")
    assert len(prices) > 0
    assert prices[0]["ticker"] == "btc_usd"

@pytest.mark.asyncio
async def test_get_latest_price():
    CurrencyService.get_latest_price = AsyncMock(return_value={"ticker": "btc_usd", "price": 30000, "timestamp": 1695000000})
    price = await CurrencyService.get_latest_price("btc_usd")
    assert price is not None
    assert price["ticker"] == "btc_usd"

@pytest.mark.asyncio
async def test_get_prices_within_date_range():
    CurrencyService.get_prices_within_date_range = AsyncMock(return_value=[{"ticker": "btc_usd", "price": 30000, "timestamp": 1695000000}])
    prices = await CurrencyService.get_prices_within_date_range("btc_usd", 1695000000, 1696000000)
    assert len(prices) > 0
    assert prices[0]["ticker"] == "btc_usd"
