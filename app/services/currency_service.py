from app.dao.currency_dao import CurrencyPriceDAO

class CurrencyService:
    @staticmethod
    async def get_all_prices(ticker: str):
        return await CurrencyPriceDAO.get_all_prices(ticker)

    @staticmethod
    async def get_latest_price(ticker: str):
        return await CurrencyPriceDAO.get_latest_price(ticker)

    @staticmethod
    async def get_prices_within_date_range(ticker: str, start_date: int, end_date: int):
        return await CurrencyPriceDAO.get_prices_within_date_range(ticker, start_date, end_date)
