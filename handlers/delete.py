from aiogram.types import Message
from loader import router, cursor, con, scheduler
from script.napominalka import napominalka_update
from aiogram import F



@router.message(F.text == "Удалить напоминалку")
async def handle_message(message: Message):
    user_id = message.from_user.id
    cursor.execute('SELECT id_task FROM users where id = (?)', (user_id,))
    data = cursor.fetchall()
    if data:
        id_task = data[0][0]
        scheduler.remove_job(id_task)
        cursor.execute('DELETE FROM users  WHERE id=(?)', (user_id,))
        con.commit()
        await message.answer(text='Всё её больше нет(')


    else:
        await message.answer(text='ВЫ ЕЩЁ ДАЖЕ НЕ ДОБАВИЛИ ССЫЛКУ!')