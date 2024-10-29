import pytest
import aiohttp
from app.clients.deribit_client import fetch_price

@pytest.mark.asyncio
async def test_fetch_price():
    async with aiohttp.ClientSession() as session:
        btc_price = await fetch_price(session, "btc_usd")
        assert btc_price is not None
        assert isinstance(btc_price, float)
        assert btc_price > 0

        eth_price = await fetch_price(session, "eth_usd")
        assert eth_price is not None
        assert isinstance(eth_price, float)
        assert eth_price > 0
