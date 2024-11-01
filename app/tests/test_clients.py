
import pytest
from unittest.mock import AsyncMock, patch
from app.clients.deribit_client import DeribitClient
import aiohttp
from aioresponses import aioresponses
import re

@pytest.mark.asyncio
@patch("app.clients.deribit_client.CurrencyDAO", autospec=True)
async def test_fetch_price_api_error(mock_currency_dao):

    base_url = "https://www.deribit.com/api/v2/public/get_index_price"
    currency = "btc_usd"
    response_payload = {"error": "Internal Server Error"}

    with aioresponses() as mocked:
        mocked.get(re.compile(r'https://www\.deribit\.com/api/v2/public/get_index_price.*'), status=500, payload=response_payload)

        deribit_client = DeribitClient()

        async with aiohttp.ClientSession() as session:
            await deribit_client.fetch_price(session, currency)

        mock_currency_dao_instance = mock_currency_dao.return_value
        mock_currency_dao_instance.save_currency_data.assert_not_called()


@pytest.mark.asyncio
@patch("app.clients.deribit_client.CurrencyDAO", autospec=True)
async def test_fetch_price_invalid_data(mock_currency_dao):

    base_url = "https://www.deribit.com/api/v2/public/get_index_price"
    currency = "btc_usd"
    response_payload = {"unexpected_key": "unexpected_value"}

    with aioresponses() as mocked:
        mocked.get(re.compile(r'https://www\.deribit\.com/api/v2/public/get_index_price.*'), status=200, payload=response_payload)

        deribit_client = DeribitClient()

        async with aiohttp.ClientSession() as session:
            await deribit_client.fetch_price(session, currency)

        mock_currency_dao_instance = mock_currency_dao.return_value
        mock_currency_dao_instance.save_currency_data.assert_not_called()
