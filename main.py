import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import handlers
from app.registration import registration
from app.authorization import authorization
from app.update_login_or_password import update_login_or_password


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(handlers)
    dp.include_router(registration)
    dp.include_router(authorization)
    dp.include_router(update_login_or_password)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
