import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import handlers
from app.registration import registration


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(handlers)
    dp.include_router(registration)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
