#!venv/bin/python
"""Main module"""
import datetime
import logging
import logging.handlers as loghandlers
import os
import sys

import telebot
from telebot import types

import config as botconf
import db
from models.model_users import User

BOT = telebot.TeleBot(botconf.BOT_TOKEN)

if not os.path.exists('logs'):
    os.makedirs('logs')
LOGGER = logging.getLogger('applog')
LOGGER.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s  %(filename)s  %(funcName)s  %(lineno)d  %(name)s  %(levelname)s: %(message)s')
log_handler = loghandlers.RotatingFileHandler(
    './logs/botlog.log',
    maxBytes=1000000,
    encoding='utf-8',
    backupCount=50
)
log_handler.setLevel(logging.INFO)
log_handler.setFormatter(formatter)
LOGGER.addHandler(log_handler)
telebot.logger.setLevel(logging.INFO)
telebot.logger.addHandler(LOGGER)


@BOT.message_handler(commands=['start'])
def cmd_start(message):
    """Старт диалога с ботом"""
    mainmenu(message)


def mainmenu(message):
    """Главное меню"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_list = []
    keyboard_list.append('Пустая кнопка')
    keyboard.add(*keyboard_list, row_width=2)

    mes = 'Добро пожаловать'
    BOT.send_message(message.chat.id, mes, reply_markup=keyboard)


if __name__ == '__main__':
    try:
        BOT.infinity_polling()
    except Exception as ex:
        LOGGER.error(ex)
        sys.exit()
