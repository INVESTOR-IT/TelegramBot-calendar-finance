from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


button_help = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Помощь')]],
    resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')

button_help_tg = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Перейти к тех поддержке', url='https://t.me/IEEE934')]
])

button_registration = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Регистрация', callback_data='registration')
]])
