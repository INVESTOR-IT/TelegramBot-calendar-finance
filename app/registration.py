from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.check as check
import hash_password as hs

registration = Router()


class Registration(StatesGroup):
    login = State()
    password = State()


@registration.callback_query(F.data == 'registration')
async def registration_one(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Начало регистрации')
    await state.set_state(Registration.login)
    await callback.message.edit_text('Введите свою почту')


@registration.message(Registration.login)
async def registration_two(message: Message, state: FSMContext):
    if await check.check_login(message.text):
        await state.update_data(login=message.text)
        await state.set_state(Registration.password)
        await message.answer('Отлично!\nВведите новый пароль\n\nПароль должен состоять из 8 символ, где должны присуствовать минимум одна строчная, заглавня буква и одна цифра')
    else:
        await message.answer('Введена некоректная почта\nПовторите попытку')


@registration.message(Registration.password)
async def registration_three(message: Message, state: FSMContext):
    answer_check = await check.check_password(message.text)
    if answer_check == True:
        await message.answer('Сохраните свой пароль!')
        await state.update_data(password=await hs.hash_password(message.text))
        data = await state.get_data()
        await message.answer('Регистрация успешно завершена', reply_markup=kb.button_object_help_profile)
        await state.clear()
        await message.answer('Для работы с вашими объектами нужно их добавить', reply_markup=kb.button_new_object)
        print(data)
    else:
        await message.answer(f'Введен некоректный пароль\n{answer_check}\nПовторите попытку')
