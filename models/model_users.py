"""Модели юзеров, ролей, итд"""
from sqlalchemy import BigInteger, Column, Date, String

from models.base import Base

# pylint: disable=missing-class-docstring,too-few-public-methods


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {"comment": "Юзеры бота"}

    id = Column(BigInteger, primary_key=True)
    fio = Column(String(100))
    datar = Column(Date)
