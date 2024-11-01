import pytest
from datetime import datetime, timedelta
from app.services.currency_service import CurrencyService
from app.models.currency_models import CurrencyData
from unittest.mock import AsyncMock
import pytz

@pytest.fixture
def currency_service():
    return CurrencyService()

@pytest.mark.asyncio
async def test_get_all_data(currency_service):
    currency_service.dao.get_all_data = AsyncMock(return_value=[
        CurrencyData(id=1, ticker="btc_usd", price=70000, timestamp=datetime.now(pytz.UTC))
    ])

    result = await currency_service.get_all_data("btc_usd")
    assert len(result) == 1
    assert result[0].ticker == "btc_usd"

@pytest.mark.asyncio
async def test_get_latest_price(currency_service):
    currency_service.dao.get_latest_price = AsyncMock(return_value=
        CurrencyData(id=1, ticker="btc_usd", price=70000, timestamp=datetime.now(pytz.UTC))
    )

    result = await currency_service.get_latest_price("btc_usd")
    assert result.ticker == "btc_usd"
    assert result.price == 70000

@pytest.mark.asyncio
async def test_get_data_by_date(currency_service):
    start_date = datetime.now(pytz.UTC) - timedelta(days=1)
    end_date = datetime.now(pytz.UTC)
    currency_service.dao.get_data_by_date = AsyncMock(return_value=[
        CurrencyData(id=1, ticker="btc_usd", price=70000, timestamp=datetime.now(pytz.UTC))
    ])

    result = await currency_service.get_data_by_date("btc_usd", start_date, end_date)
    assert len(result) == 1
    assert result[0].ticker == "btc_usd"
