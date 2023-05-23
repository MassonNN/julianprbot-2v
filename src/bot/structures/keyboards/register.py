from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

REGISTER_START_CONFIRM = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Начать регистрацию')]
    ],
    resize_keyboard=True
)

REGISTER_SELECT_ROLE = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Я хочу покупать рекламу')],
        [KeyboardButton(text='Я владелец канала(ов) и хочу продавать рекламу')]
    ],
    resize_keyboard=True
)

REGISTER_RULES_READ = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text='Подтверждаю, что согласен(сна) с правилами', callback_data='read_rules')
    ]]
)