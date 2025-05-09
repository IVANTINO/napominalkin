from aiogram import Bot, Dispatcher, Router
from config.token import TOKEN
from aiogram.types import Message
import sqlite3
from apscheduler.schedulers.asyncio import AsyncIOScheduler

con = sqlite3.connect("data.db")
cursor = con.cursor()

router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)
scheduler=AsyncIOScheduler(timezone='Europe/Moscow')