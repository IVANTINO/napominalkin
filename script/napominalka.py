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
    cursor.execute(f'SELECT time FROM users where id = (?)', [user_id])
    a = cursor.fetchall()
    h = datetime.now().hour
    m = datetime.now().minute
    n = 0
    min = a[n][0][3:]
    hour = a[n][0][:2]
    print(a)
    n = 0
    l = len(a)
    print(h, m)
    for n in range(0, l):
        print(hour, h)
        if int(h) == int(hour):
            print(m)
            if int(m) == int(min):
                print(min)
                cursor.execute(f'SELECT task FROM users WHERE time=(?)', [a[n][0]])
                print(cursor.fetchall())
            else:
                n += 1
        else:
            n += 1
