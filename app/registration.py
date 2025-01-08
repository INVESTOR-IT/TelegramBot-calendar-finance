from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

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
    await state.update_data(login=message.text)
    await state.set_state(Registration.password)
    await message.answer('Отлично!\n Введите новый пароль:')


@registration.message(Registration.password)
async def registration_three(message: Message, state: FSMContext):
    await message.answer('Сохраните свой пароль!')
    await state.update_data(password=message.text)
    data = await state.get_data()
    await message.answer('Регистрация успешно завершена', reply_markup=kb.button_object_help_profile)
    await state.clear()
    await message.answer('Для работы с вашими объектами нужно их добавить', reply_markup=kb.button_new_object)
