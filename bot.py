import logging
import asyncio
from loader import *
from datetime import datetime

import handlers.start
import handlers.add


async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())




if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
