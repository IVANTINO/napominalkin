from aiogram import types

kb_start =[
    types.KeyboardButton(text='Добавить напоминалку'),
    types.KeyboardButton(text='Удалить напоминалку')
]

kb_type =[
    types.KeyboardButton(text='Ежедневно'),
    types.KeyboardButton(text='В определённые дни недели'),
    types.KeyboardButton(text='В определённую дату')
]