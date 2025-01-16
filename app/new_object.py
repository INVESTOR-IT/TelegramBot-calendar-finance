from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.sql as sql
import config

new_object = Router()


class NewObject(StatesGroup):
    name_object = State()
    type_objects = State()
    address = State()


#########################################################################################
# Добавление нового объекта
@new_object.callback_query(F.data == 'new object')
async def new_object_name(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Добавляем новый объект')
    await callback.message.answer('Объект добавляется в 3-и шага:\n'
                                  '  1. Укажите тип объекта\n'
                                  '  2. Укажите адрес объекта\n'
                                  '  3. Дайте название вашему оъекту\n\n'
                                  'Начнем с первого шага, выберите тип объекта',
                                  reply_markup=kb.button_type_object)
    await state.set_state(NewObject.type_objects)


@new_object.message(NewObject.type_objects)
async def new_object_type(message: Message, state: FSMContext):
    if message.text in ('Студия', 'Загородный дом', '1 комнатная квартира',
                        'Евродвушка', '2 комнатная квартира', '3 комнатная квартира'):
        await state.update_data(type_objects=message.text)
        await state.set_state(NewObject.address)
        await message.answer('Отлично, теперь введите адрес объекта\n\n'
                             'Пример: Москва, ул. Газопровод, 4Б')
    else:
        await message.answer('Выберите иммено из пункта меню тип объекта',
                             reply_markup=kb.button_type_object)


@new_object.message(NewObject.address)
async def new_object_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer('Записал!\nТеперь дайте название объекта.\n'
                         'Его никто не увидит, это для вашего удобства.\n'
                         'Название будет отображаться при выборе объекта в календаре')
    await state.set_state(NewObject.name_object)


@new_object.message(NewObject.name_object)
async def new_object_name(message: Message, state: FSMContext):
    await state.update_data(name_object=message.text)
    data_object = await state.get_data()
    await state.clear()
    sql.insert("INSERT INTO Objects (id, id_user, type_objects, address, name_object)"
               f"VALUES (NULL, {config.USER}, '{data_object['type_objects']}', '{data_object['address']}', '{data_object['name_object']}')")
    await message.answer('Готово! Теперь ваш объект можно выбрать в календаре', reply_markup=kb.button_object_help_profile)
