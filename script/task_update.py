from  loader import cursor, bot, scheduler, con
from script.napominalka import napominalka_update

async def task_update(user_id, message):
    cursor.execute("SELECT id, id_task FROM users")
    cursor.fetchall()

    scheduler.start()


