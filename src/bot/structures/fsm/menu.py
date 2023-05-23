from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

MENU_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Мои посты'), KeyboardButton(text='Мои каналы')],
        [KeyboardButton(text='Помощь'), KeyboardButton(text='Баланс')],
    ],
    resize_keyboard=True
)