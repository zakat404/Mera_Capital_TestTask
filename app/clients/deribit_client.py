# app/clients/deribit_client.py

import aiohttp
import asyncio
import logging
import time
from app.dao.currency_dao import CurrencyDAO
from app.models.currency_models import CurrencyDataModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DeribitClient:
    def __init__(self):
        self.base_url = "https://www.deribit.com/api/v2/public/get_index_price"
        self.currencies = ["btc_usd", "eth_usd"]
        self.dao = CurrencyDAO()

    async def fetch_price(self, session: aiohttp.ClientSession, currency: str):
        try:
            params = {"index_name": currency.upper()}
            async with session.get(self.base_url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    if "result" in data and "index_price" in data["result"]:
                        price = data["result"]["index_price"]
                        timestamp = int(time.time())
                        currency_data = CurrencyDataModel(
                            ticker=currency, price=price, timestamp=timestamp
                        )
                        await self.dao.save_currency_data(currency_data)
                        logger.info(f"Fetched price for {currency}: {price}")
                    else:
                        logger.warning(f"Unexpected data format for {currency}: {data}")
                else:
                    logger.error(f"Failed to fetch data for {currency}. Status code: {response.status}")
        except Exception as e:
            logger.exception(f"Exception occurred while fetching price for {currency}: {e}")

    async def start_fetching(self):
        while True:
            async with aiohttp.ClientSession() as session:
                tasks = [
                    self.fetch_price(session, currency) for currency in self.currencies
                ]
                await asyncio.gather(*tasks)
            await asyncio.sleep(60)
