from datetime import datetime

from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_start
from loader import router
from datetime import datetime
import sqlite3

con = sqlite3.connect('data.db', check_same_thread=False)
cursor = con.cursor()



@router.message(Command('start'))
async def fun_start(message: Message):

    builder = ReplyKeyboardBuilder()
    for button in kb_start:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text='Привет, рад тебя видеть! Этот бот может помочь тебе запомнить базовые вещи кторые постоянно вылетают из головы!',
                            reply_markup=builder.as_markup(resize_keyboard=True))
