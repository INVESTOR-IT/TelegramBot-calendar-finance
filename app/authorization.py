from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.check as check
import app.sql as sql
import hash_password as hs
import config

authorization = Router()


class Authorization(StatesGroup):
    login = State()
    password = State()


#########################################################################################
# Авторизация пользователя
@authorization.callback_query(F.data == 'authorization')
async def authorization_one(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Начало авторизации')
    await state.set_state(Authorization.login)
    await callback.message.edit_text('Введите свой логин')


@authorization.message(Authorization.login)
async def authorization_two(message: Message, state: FSMContext):
    if await check.check_login(message.text):
        if sql.select(f"SELECT * FROM User WHERE email = '{message.text}'"):
            await state.update_data(login=message.text)
            await state.set_state(Authorization.password)
            await message.answer('Отлично! Введите свой пароль')
        else:
            await message.answer('С такой почтой данного пользователя нет\n'
                                 'Проверьте корректность введенной почты и повторите попытку или зарегистрируйтесь',
                                 reply_markup=kb.button_authorization_registration)
    else:
        await message.answer('Введена некоректная почта\nПовторите попытку')


@authorization.message(Authorization.password)
async def authorization_three(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    data_user = await state.get_data()
    await state.clear()
    data = sql.select(f"SELECT * FROM User WHERE email = '{data_user['login']}'")[0]
    if data['hash_password'] == await hs.hash_password(data_user['password']):
        config.USER = sql.select(f"SELECT id FROM User WHERE email = '{data_user['login']}'")[0]['id']
        await message.answer('Вы успешно вошли', reply_markup=kb.button_object_calendar_help_profile)
    else:
        await message.answer('Пароль введен не верно, повторите попытку и проверьте почту',
                             reply_markup=kb.button_authorization_registration)
