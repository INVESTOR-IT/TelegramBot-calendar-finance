from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb


handlers = Router()


@handlers.message(CommandStart())
async def start(message: Message):
    await message.answer('Добро пожаловать в календарь', reply_markup=kb.button_help)
    await message.answer('Что бы добавить свои объекты, нужно зарегистрироваться', reply_markup=kb.button_registration)


@handlers.message(F.text == 'Помощь')
async def help(message: Message):
    print(1)
    await message.answer('Сообщите мне об ошибке', reply_markup=kb.button_help_tg)
