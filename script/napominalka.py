from datetime import datetime
from os.path import split

from aiogram.types import WebAppInfo
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bs4 import BeautifulSoup
from loader import cursor, bot
from aiogram import types
from loader import *


async def napominalka_update(user_id, bot, message):
    print(1)
    cursor.execute(f'SELECT time FROM users where id = (?)', [user_id])
    a=cursor.fetchall()













