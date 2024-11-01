from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.database import Base
from pydantic import BaseModel, ConfigDict
from datetime import datetime
class CurrencyDataModel(Base):
    __tablename__ = "currency_data"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    price = Column(Float)
    timestamp = Column(DateTime(timezone=True), index=True)


class CurrencyData(BaseModel):
    id: int
    ticker: str
    price: float
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)

