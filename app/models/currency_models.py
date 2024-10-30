# app/models/currency.py

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class CurrencyDataModel(Base):
    __tablename__ = "currency_data"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    price = Column(Float)
    timestamp = Column(Integer, index=True)


class CurrencyData(BaseModel):
    ticker: str
    price: float
    timestamp: int

    class Config:
        orm_mode = True
