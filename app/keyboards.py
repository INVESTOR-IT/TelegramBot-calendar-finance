from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


#########################################################################################
# Кнопка помощь над клавиатурой
button_help = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Помощь')]],
    resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')


#########################################################################################
# Кнопка помощь под сообщением с ТГ
button_help_tg = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Перейти к тех поддержке', url='https://t.me/IEEE934')]])


#########################################################################################
# Кнопи авторизация и регистрация под сообщением
button_authorization_registration = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Войти', callback_data='authorization')],
    [InlineKeyboardButton(text='Регистрация', callback_data='registration')]])


#########################################################################################
# Кнопки объекты, помощь, профиль над клавиатурой (БАЗА)
button_object_calendar_help_profile = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Объекты'), KeyboardButton(text='Календарь')],
    [KeyboardButton(text='Помощь'), KeyboardButton(text='Профиль')]],
    resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')


#########################################################################################
# Кнопка добавить объект под сообщением
button_new_object = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить объект', callback_data='new object')]])


#########################################################################################
# Кнопки о смене логина или пароля под сообщением
button_update_profile = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Изменить почту', callback_data='update email')],
    [InlineKeyboardButton(text='Изменить пароль', callback_data='new password')]])


#########################################################################################
# Кнопки типов объекта
button_type_object = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Студия'), KeyboardButton(text='Загородный дом')],
    [KeyboardButton(text='1 комнатная квартира'), KeyboardButton(text='Евродвушка')],
    [KeyboardButton(text='2 комнатная квартира'), KeyboardButton(text='3 комнатная квартира')]],
    resize_keyboard=True, input_field_placeholder='Выберите тип объекта...')


#########################################################################################
# Все объекты пользователя
async def all_objects(objects: tuple):
    builder = InlineKeyboardBuilder()
    for my_id, my_object in objects:
        builder.add(InlineKeyboardButton(text=my_object, callback_data=f'update_object_{my_id}'))
    builder.add(InlineKeyboardButton(text='Добавить объект', callback_data='new object'))
    return builder.adjust(1).as_markup()


#########################################################################################
# Изменить объект
button_update_object = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Изменить имя', callback_data='update_name_object')],
    [InlineKeyboardButton(text='Изменить тип', callback_data='update_type_object')],
    [InlineKeyboardButton(text='Изменить адрес', callback_data='update_address_object')]])
