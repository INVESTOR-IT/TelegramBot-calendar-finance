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
    await message.answer('Что бы добавить свои объекты, нужно зарегистрироваться',
                         reply_markup=kb.button_authorization_registration)


#########################################################################################
# Зайти как разработчик
@handlers.message(Command('q1'))
async def developer(message: Message):
    config.USER = 1
    await message.answer('Вошел как разраб',
                         reply_markup=kb.button_object_calendar_help_profile)


#########################################################################################
# Помощь
@handlers.message(F.text == 'Помощь')
async def help(message: Message):
    await message.answer('Сообщите мне об ошибке', reply_markup=kb.button_help_tg)


#########################################################################################
# Все объекты пользователя
@handlers.message(F.text == 'Объекты')
async def objects(message: Message):
    name_objects = sql.select("SELECT id, name_object FROM Objects "
                              f"WHERE id_user = '{config.USER}'")

    if name_objects:
        name_objects = tuple((name['id'], name['name_object']) for name in name_objects)
        await message.answer('Ваши объекты', reply_markup=await kb.all_objects(name_objects))
    else:
        await message.answer('У вас нет объектов', reply_markup=kb.button_new_object)


#########################################################################################
# Профиль пользователя
@handlers.message(F.text == 'Профиль')
async def profile(message: Message):
    info_user = sql.select("SELECT User.id, email, COUNT(Objects.id) as count, data_registration FROM User "
                           "LEFT OUTER JOIN Objects ON User.id = Objects.id_user "
                           "GROUP BY User.id, email "
                           f"HAVING User.id = '{config.USER}'")[0]

    await message.answer(f"Дата регистрации: {info_user['data_registration']}\n"
                         f"Ваша почта: {info_user['email']}\n\n"
                         f"Количество объектов: {info_user['count']}",
                         reply_markup=kb.button_update_profile)


#########################################################################################
# Календарь пользователя
@handlers.message(F.text == 'Календарь')
async def calendar(message: Message):
    await message.answer('В разработке',
                         reply_markup=kb.button_object_calendar_help_profile)
