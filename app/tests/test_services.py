# app/tests/test_services.py

import pytest
from app.services.currency_service import CurrencyService

@pytest.mark.asyncio
async def test_get_all_data():
    service = CurrencyService()
    data = await service.get_all_data("btc_usd")
    assert isinstance(data, list)
