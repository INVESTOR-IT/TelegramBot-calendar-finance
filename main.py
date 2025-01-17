import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import handlers
from app.registration import registration
from app.authorization import authorization
from app.update_login_or_password import update_login_or_password
from app.new_object import new_object
from app.update_object import update_object


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(handlers)
    dp.include_router(registration)
    dp.include_router(authorization)
    dp.include_router(update_login_or_password)
    dp.include_router(new_object)
    dp.include_router(update_object)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
