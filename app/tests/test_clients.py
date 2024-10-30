# app/tests/test_clients.py

import pytest
import asyncio
from app.clients.deribit_client import DeribitClient

@pytest.mark.asyncio
async def test_fetch_price():
    client = DeribitClient()
    async with client:
        async with aiohttp.ClientSession() as session:
            await client.fetch_price(session, "btc_usd")
            await client.fetch_price(session, "eth_usd")
    # Дополнительно можно проверить, что данные сохранены в базе данных
