from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


button_help = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Помощь')]],
    resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')

button_help_tg = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Перейти к тех поддержке', url='https://t.me/IEEE934')]])

button_authorization_registration = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Войти', callback_data='authorization')],
    [InlineKeyboardButton(text='Регистрация', callback_data='registration')]])

button_object_help_profile = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Объекты'), KeyboardButton(text='Помощь')],
    [KeyboardButton(text='Профиль')]],
    resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')

button_new_object = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить объект', callback_data='new object')]])

button_update_profile = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Изменить почту', callback_data='update email')],
    [InlineKeyboardButton(text='Изменить пароль', callback_data='new password')]])
