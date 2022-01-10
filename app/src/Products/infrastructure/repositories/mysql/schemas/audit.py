from ..connection_provider import Base
from sqlalchemy import Column, Integer, String


class Audit(Base):
    __tablename__ = 'audit'

    audit_id = Column(Integer, primary_key=True)
    ip = Column(String(20))
    product_id = Column(Integer)
