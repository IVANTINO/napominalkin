from aiogram import types

kb_start =[
    types.KeyboardButton(text='Добавить напоминалку'),
    types.KeyboardButton(text='Удалить напоминалку')
]

kb_type =[
    types.KeyboardButton(text='Ежедневно'),
    types.KeyboardButton(text='В определённый день недели'),
    types.KeyboardButton(text='В один определённый день')
]

kb_days =[
    types.KeyboardButton(text='Понедельник'),
    types.KeyboardButton(text='Вторник'),
    types.KeyboardButton(text='Среда'),
    types.KeyboardButton(text='Четверг'),
    types.KeyboardButton(text='Пятница'),
    types.KeyboardButton(text='Суббота'),
    types.KeyboardButton(text='Воскресенье')
]
