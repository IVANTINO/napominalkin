import requests
from datetime import datetime
from aiogram.types import WebAppInfo
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bs4 import BeautifulSoup
from loader import cursor, bot
from aiogram import types
from loader import *


async def napominalka_update(user_id, bot, message):
    cursor.execute(f'SELECT * FROM users where id = (?)', [user_id])
    cursor.fetchall()
    now_hour=datetime.time().hour



