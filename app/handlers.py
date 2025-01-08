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
    await message.answer('Сообщите мне об ошибке', reply_markup=kb.button_help_tg)


@handlers.message(F.text == 'Объекты')
async def objects(message: Message):
    await message.answer('Нет запроса')


@handlers.message(F.text == 'Профиль')
async def profile(message: Message):
    await message.answer('Ваша почта: </>\n\nКоличество объектов: </>', reply_markup=kb.button_update_profile)


@handlers.callback_query(F.data == 'new object')
async def new_object(callback: CallbackQuery):
    await callback.answer('Добавляем новый объект')
    await callback.message.answer('_/O\_')
