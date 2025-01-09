from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.check as check

authorization = Router()


class Authorization(StatesGroup):
    login = State()
    password = State()


@authorization.callback_query(F.data == 'authorization')
async def authorization_one(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Начало авторизации')
    await state.set_state(Authorization.login)
    await callback.message.edit_text('Введите свой логин')


@authorization.message(Authorization.login)
async def authorization_two(message: Message, state: FSMContext):
    if check.check_login(message.text):
        await state.update_data(login=message.text)
        await state.set_state(Authorization.password)
        await message.answer('Введите свой пароль')
    else:
        await message.answer('Введена некоректная почта\nПовторите попытку')


@authorization.message(Authorization.password)
async def authorization_three(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    await state.clear()
    await message.answer('Вы успешно вошли', reply_markup=kb.button_object_help_profile)
