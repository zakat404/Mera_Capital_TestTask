# app/services/currency_service.py

from typing import List
from app.dao.currency_dao import CurrencyDAO
from app.models.currency_models import CurrencyData

class CurrencyService:
    def __init__(self):
        self.dao = CurrencyDAO()

    async def get_all_data(self, ticker: str) -> List[CurrencyData]:
        return await self.dao.get_all_data(ticker)

    async def get_latest_price(self, ticker: str) -> CurrencyData:
        return await self.dao.get_latest_price(ticker)

    async def get_data_by_date(
        self, ticker: str, start_date: int, end_date: int
    ) -> List[CurrencyData]:
        return await self.dao.get_data_by_date(ticker, start_date, end_date)
