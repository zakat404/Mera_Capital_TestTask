import aiohttp
import asyncio
import time
from app.models.currency_models import CurrencyPrice
from app.db.database import async_session

DERIBIT_API_URL = "https://www.deribit.com/api/v2/public/get_index_price"

async def fetch_price(session, ticker):
    params = {"index_name": ticker}
    async with session.get(DERIBIT_API_URL, params=params) as response:
        data = await response.json()
        return data["result"]["index_price"]

async def fetch_prices():
    async with aiohttp.ClientSession() as session:
        btc_price = await fetch_price(session, "btc_usd")
        eth_price = await fetch_price(session, "eth_usd")
        timestamp = int(time.time())

        async with async_session() as db_session:
            for ticker, price in [("btc_usd", btc_price), ("eth_usd", eth_price)]:
                db_session.add(CurrencyPrice(ticker=ticker, price=price, timestamp=timestamp))
            await db_session.commit()

async def schedule_price_fetch():
    while True:
        await fetch_prices()
        await asyncio.sleep(60)


