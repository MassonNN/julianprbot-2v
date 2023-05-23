from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton

from src.api.payment import PaymentCase, get_payment_url


def get_payment_keyboard(payment_case: PaymentCase) -> InlineKeyboardButton:
    return InlineKeyboardButton(keyboard=[
        [InlineKeyboardButton(f'Пополнить аккаунт на {payment_case.value}$', url=get_payment_url(payment_case))]
    ])
