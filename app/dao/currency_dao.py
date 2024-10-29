from app.db.database import async_session
from sqlalchemy import select, desc
from app.models.currency_models import CurrencyPrice

class CurrencyPriceDAO:
    @staticmethod
    async def get_all_prices(ticker: str):
        async with async_session() as session:
            query = select(CurrencyPrice).where(CurrencyPrice.ticker == ticker)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_latest_price(ticker: str):
        async with async_session() as session:
            query = select(CurrencyPrice).where(CurrencyPrice.ticker == ticker).order_by(desc(CurrencyPrice.timestamp))
            result = await session.execute(query)
            return result.scalars().first()

    @staticmethod
    async def get_prices_within_date_range(ticker: str, start_date: int, end_date: int):
        async with async_session() as session:
            query = select(CurrencyPrice).where(
                (CurrencyPrice.ticker == ticker) &
                (CurrencyPrice.timestamp >= start_date) &
                (CurrencyPrice.timestamp <= end_date)
            )
            result = await session.execute(query)
            return result.scalars().all()

