# app/clients/deribit_client.py

import aiohttp
import asyncio
import time
from app.dao.currency_dao import CurrencyDAO
from app.models.currency_models import CurrencyDataModel
from app.config.settings import settings

class DeribitClient:
    def __init__(self):
        self.base_url = "https://www.deribit.com/api/v2/public/get_index_price"
        self.currencies = ["btc_usd", "eth_usd"]
        self.dao = CurrencyDAO()

    async def fetch_price(self, session: aiohttp.ClientSession, currency: str):
        params = {"index_name": currency.upper()}
        async with session.get(self.base_url, params=params) as response:
            data = await response.json()
            price = data["result"]["index_price"]
            timestamp = int(time.time())
            currency_data = CurrencyDataModel(
                ticker=currency, price=price, timestamp=timestamp
            )
            await self.dao.save_currency_data(currency_data)

    async def start_fetching(self):
        while True:
            async with aiohttp.ClientSession() as session:
                tasks = [
                    self.fetch_price(session, currency) for currency in self.currencies
                ]
                await asyncio.gather(*tasks)
            await asyncio.sleep(60)
