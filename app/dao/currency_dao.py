# app/dao/currency_dao.py

from typing import List
from sqlalchemy.future import select
from sqlalchemy import desc
from app.db.database import async_session
# from app.models.currency import CurrencyDataModel, CurrencyData
from app.models.currency_models import CurrencyData, CurrencyDataModel


class CurrencyDAO:
    async def save_currency_data(self, data: CurrencyDataModel):
        async with async_session() as session:
            session.add(data)
            await session.commit()

    async def get_all_data(self, ticker: str) -> List[CurrencyData]:
        async with async_session() as session:
            result = await session.execute(
                select(CurrencyDataModel).where(CurrencyDataModel.ticker == ticker)
            )
            data = result.scalars().all()
            return [CurrencyData.from_orm(d) for d in data]

    async def get_latest_price(self, ticker: str) -> CurrencyData:
        async with async_session() as session:
            result = await session.execute(
                select(CurrencyDataModel)
                .where(CurrencyDataModel.ticker == ticker)
                .order_by(desc(CurrencyDataModel.timestamp))
                .limit(1)
            )
            data = result.scalar_one_or_none()
            if data:
                return CurrencyData.from_orm(data)
            return None

    async def get_data_by_date(
        self, ticker: str, start_date: int, end_date: int
    ) -> List[CurrencyData]:
        async with async_session() as session:
            result = await session.execute(
                select(CurrencyDataModel)
                .where(CurrencyDataModel.ticker == ticker)
                .where(CurrencyDataModel.timestamp >= start_date)
                .where(CurrencyDataModel.timestamp <= end_date)
            )
            data = result.scalars().all()
            return [CurrencyData.from_orm(d) for d in data]
