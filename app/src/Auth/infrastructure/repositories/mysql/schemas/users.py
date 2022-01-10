from ..connection_provider import Base
from sqlalchemy import Column, Integer, String, Boolean


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    email = Column(String(150))
    password = Column(String(200))
    is_admin = Column(Boolean)
