"""Юзеры"""
import logging

from db.connection import Session
from models.model_users import User

LOGGER = logging.getLogger('applog')


def get_users_tuple():
    """Все юзеры"""
    session = Session()
    values_tuple = session.query(User).all()
    session.close()
    return values_tuple
