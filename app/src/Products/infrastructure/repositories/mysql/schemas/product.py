from .....domain.constants import State
from ..connection_provider import Base
from sqlalchemy import Column, Integer, String, Float, SmallInteger


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    sku = Column(String(100))
    price = Column(Float(8, 2))
    brand = Column(String(100))
    state = Column(SmallInteger, default=State.ACTIVE.value)
