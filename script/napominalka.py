import requests
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bs4 import BeautifulSoup
from loader import cursor, Bot
import json
from aiogram import types


async def napominalka_update(user_id, bot: Bot):
    print('kek')
