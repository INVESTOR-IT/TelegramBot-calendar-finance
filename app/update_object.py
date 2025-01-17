from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.sql as sql
import app.keyboards as kb


update_object = Router()
id_object = None


class UpdateObject(StatesGroup):
    name = State()
    type_object = State()
    address = State()


#########################################################################################
# Информация об объекте
@update_object.callback_query(F.data.startswith('update_object'))
async def info_object(callback: CallbackQuery):
    global id_object
    await callback.answer('Информация об объекте')
    my_object = sql.select("SELECT * FROM Objects "
                           f"WHERE id = '{callback.data.split('_')[2]}'")[0]
    id_object = my_object['id']
    await callback.message.answer(f"{my_object['name_object'].upper()}\n\n"
                                  f"Тип объекта: {my_object['type_objects']}\n"
                                  f"Адрес объекта: {my_object['address']}",
                                  reply_markup=kb.button_update_object)


#########################################################################################
# Меняем имя объекта
@update_object.callback_query(F.data == 'update_name_object')
async def update_name_object_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Смена имени объекта')
    await state.set_state(UpdateObject.name)
    await callback.message.answer('Введите новое имя')


@update_object.message(UpdateObject.name)
async def update_name_object_end(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    name = await state.get_data()
    await state.clear()
    sql.update("UPDATE Objects "
               f"SET name_object = '{name['name']}' "
               f"WHERE id = {id_object}")
    await message.answer('Готово, обновили имя объекта',
                         reply_markup=kb.button_object_calendar_help_profile)


#########################################################################################
# Меняем тип объекта
@update_object.callback_query(F.data == 'update_type_object')
async def update_type_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Смена типа объекта')
    await state.set_state(UpdateObject.type_object)
    await callback.message.answer('Выберите новый тип данных',
                                  reply_markup=kb.button_type_object)


@update_object.message(UpdateObject.type_object)
async def update_type_end(message: Message, state: FSMContext):
    if message.text in ('Студия', 'Загородный дом', '1 комнатная квартира',
                        'Евродвушка', '2 комнатная квартира', '3 комнатная квартира'):
        await state.update_data(type_object=message.text)
        type_object = await state.get_data()
        await state.clear()
        sql.update("UPDATE Objects "
                   f"SET type_objects = '{type_object['type_object']}' "
                   f"WHERE id = {id_object}")
        await message.answer('Готово!\nОбновили тип объекта',
                             reply_markup=kb.button_object_calendar_help_profile)


#########################################################################################
# Меняем адрес объекта
@update_object.callback_query(F.data == 'update_address_object')
async def update_address_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Смена одреса объекта')
    await state.set_state(UpdateObject.address)
    await callback.message.answer('Ввкдите новый адрес\n\n'
                                  'Пример: Москва, ул. Газопровод, 4Б')


@update_object.message(UpdateObject.address)
async def update_address_end(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    address = await state.get_data()
    await state.clear()
    sql.update("UPDATE Objects "
               f"SET address = '{address['address']}' "
               f"WHERE id = {id_object}")
    await message.answer('Готово!\nИзменили адрес объекта',
                         reply_markup=kb.button_object_calendar_help_profile)
