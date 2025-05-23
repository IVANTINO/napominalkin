import logging
import asyncio
from loader import *
from script.task_update import task_update

import handlers.start
import handlers.add


async def main():

    scheduler.start()
    task_update()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())






if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
