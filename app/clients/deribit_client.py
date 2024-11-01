# app/clients/deribit_client.py
import aiohttp
import asyncio
import logging
from datetime import datetime
import pytz
from app.dao.currency_dao import CurrencyDAO
from app.models.currency_models import CurrencyDataModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DeribitClient:
    def __init__(self):
        self.base_url = "https://www.deribit.com/api/v2/public/get_index_price"
        self.currencies = ["btc_usd", "eth_usd"]
        self.dao = CurrencyDAO()
        self._fetching_task = None
        self._stop_event = asyncio.Event()

    async def fetch_price(self, session: aiohttp.ClientSession, currency: str):
        try:
            params = {"index_name": currency}
            async with session.get(self.base_url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Full response for {currency}: {data}")
                    if "result" in data and "index_price" in data["result"]:
                        price = data["result"]["index_price"]

                        tz = pytz.timezone('Europe/Moscow')
                        timestamp = datetime.now(tz)

                        currency_data = CurrencyDataModel(
                            ticker=currency,
                            price=price,
                            timestamp=timestamp
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
        self._fetching_task = asyncio.create_task(self._run())

    async def _run(self):
        while not self._stop_event.is_set():
            async with aiohttp.ClientSession() as session:
                tasks = [
                    self.fetch_price(session, currency) for currency in self.currencies
                ]
                await asyncio.gather(*tasks)
            await asyncio.sleep(60)

    def stop_fetching(self):
        self._stop_event.set()
        if self._fetching_task:
            self._fetching_task.cancel()
