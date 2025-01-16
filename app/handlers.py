from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb
import app.sql as sql
import config


handlers = Router()


#########################################################################################
# Старт бота
@handlers.message(CommandStart())
async def start(message: Message):
    await message.answer('Добро пожаловать в календарь', reply_markup=kb.button_help)
    await message.answer('Что бы добавить свои объекты, нужно зарегистрироваться', reply_markup=kb.button_authorization_registration)


#########################################################################################
# Помощь
@handlers.message(F.text == 'Помощь')
async def help(message: Message):
    await message.answer('Сообщите мне об ошибке', reply_markup=kb.button_help_tg)


#########################################################################################
# Все объекты пользователя
@handlers.message(F.text == 'Объекты')
async def objects(message: Message):
    await message.answer('Нет запроса')


#########################################################################################
# Профиль пользователя
@handlers.message(F.text == 'Профиль')
async def profile(message: Message):
    info_user = sql.select("SELECT User.id, email, COUNT(Objects.id) as count, data_registration FROM User " \
                            "LEFT OUTER JOIN Objects ON User.id = Objects.id_user " \
                            "GROUP BY User.id, email " \
                            f"HAVING User.id = '{config.USER}'")[0]
    
    await message.answer(f"Дата регистрации: {info_user['data_registration']}\n" \
                         f"Ваша почта: {info_user['email']}\n\n" \
                         f"Количество объектов: {info_user['count']}", reply_markup=kb.button_update_profile)


#########################################################################################
# Новый объект пользователя
@handlers.callback_query(F.data == 'new object')
async def new_object(callback: CallbackQuery):
    await callback.answer('Добавляем новый объект')
    await callback.message.answer('_/O\_')
