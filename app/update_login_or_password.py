from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.check as check
import app.keyboards as kb
import hash_password as hs

update_login_or_password = Router()


class Update_login(StatesGroup):
    login = State()


class Update_password(StatesGroup):
    password = State()


@update_login_or_password.callback_query(F.data == 'update email')
async def update_login_one(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Смена логина')
    await state.set_state(Update_login.login)
    await callback.message.answer('Введите новую почту')


@update_login_or_password.message(Update_login.login)
async def update_login_two(message: Message, state: FSMContext):
    if await check.check_login(message.text):
        await state.update_data(login=message.text)
        login = await state.get_data()
        await state.clear()
        await message.answer('Почта успешно обновлена!', reply_markup=kb.button_object_help_profile)
    else:
        await message.answer('Введена некоректная почта\nПовторите попытку')


@update_login_or_password.callback_query(F.data == 'new password')
async def new_password_one(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Смена пароля')
    await state.set_state(Update_password.password)
    await callback.message.answer('Введите новый пароль\n\nПароль должен состоять из 8 символ, где должны присуствовать минимум одна строчная, заглавня буква и одна цифра')


@update_login_or_password.message(Update_password.password)
async def new_password_two(message: Message, state: FSMContext):
    answer_check = await check.check_password(message.text)
    if answer_check == True:
        await state.update_data(password=await hs.hash_password(message.text))
        password = await state.get_data()
        await state.clear()
        await message.answer('Пароль успешно обновлен', reply_markup=kb.button_object_help_profile)
    else:
        await message.answer(f'Введен некоректный пароль\n{answer_check}\nПовторите попытку')
