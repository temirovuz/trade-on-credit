from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import Session

from core.database import Base


class Customer(Base):
    id = Column(Integer, primary_key=True)
    shop_id = Column(Integer, ForeignKey('shop.id'))
    name = Column(String(120))
    phone_number = Column(String(13), primary_key=True)
    price = Column(Integer)

# ---------------------------------->   create      <--------------------------------- #
