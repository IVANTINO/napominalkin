from  loader import cursor, bot, scheduler, con
from script.napominalka import napominalka_update

def task_update():
    cursor.execute("SELECT * FROM users")
    data=cursor.fetchall()
    user_id=data[0][0][0]

    for user in data:
        task_id = scheduler.add_job(napominalka_update,
                                    trigger='cron',
                                    hour=19,
                                    minute=47,
                                    kwargs=user_id)






