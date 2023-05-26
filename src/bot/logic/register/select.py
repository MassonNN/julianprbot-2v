from _decimal import Decimal
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from src.api.payment import PaymentCase
from .router import register_router
from ...add_channel import add_channel
from ...structures.fsm.register import RegisterGroup, RegisterForBuyer, RegisterForSeller
from ...structures.keyboards.payment import get_payment_keyboard
from ...structures.keyboards.register import REGISTER_SELECT_ROLE, REGISTER_RULES_READ
from ...structures.role import ProfileType


@register_router.message(F.text == 'Начать регистрацию', RegisterGroup.confirmation)
async def register_confirmation(message: Message, state: FSMContext):
    await state.set_state(RegisterGroup.select)
    return await message.answer(
        'Выбери тип своего профиля',
        reply_markup=REGISTER_SELECT_ROLE
    )


@register_router.message(F.text == 'Я хочу покупать рекламу', RegisterGroup.select)
async def register_confirmation(message: Message, state: FSMContext):
    await state.update_data({
        'role': ProfileType.BUYER
    })
    await state.set_state(RegisterForBuyer.rules)
    return await message.answer('Ознакомьтесь с нашими правилами', reply_markup=REGISTER_RULES_READ)


@register_router.message(F.text == 'Я владелец канала(ов) и хочу продавать рекламу', RegisterGroup.select)
async def register_confirmation(message: Message, state: FSMContext):
    await state.update_data({
        'role': ProfileType.SELLER
    })
    await state.set_state(RegisterForSeller.rules)
    return await message.answer('Ознакомьтесь с нашими правилами', reply_markup=REGISTER_RULES_READ)


@register_router.callback_query(F.data == 'read_rules', RegisterForSeller.rules)
async def read_rules(call: CallbackQuery, state: FSMContext):
    await state.set_state(RegisterForSeller.add_tg_channel)
    return await call.message.answer(
        'Для продолжения регистрации необходимо добавить хотя бы один телеграмм канал. '
        'Отправь ссылку на свой канал мне для дальнейшей регистрации. '
        'Твой канал должен удовлетворять следующим критериям:\n'
        '- В нем должно быть более 100 подписчиков\n'
        '- Его содержание не должно нарушать законы твоей страны\n\n'
        'Проверка будет проводиться вручную модераторами, это потребует времени.'
    )


@register_router.message(RegisterForSeller.add_tg_channel)
async def add_tg_channel(message: Message, state: FSMContext):
    await state.clear()
    await add_channel(message.from_user, message.text)
    return await message.answer('Твой канал отправлен в очередь на проверку модерацией!\nПосле его проверки мы '
                                'отправим тебе сообщение.')


@register_router.callback_query(F.data == 'read_rules', RegisterForBuyer.rules)
async def read_rules(call: CallbackQuery, state: FSMContext):
    await state.set_state(RegisterForBuyer.fund)
    p_case = PaymentCase(user_id=call.from_user.id, value=Decimal(5))
    return await call.message.answer(
        'Для продолжения регистрации необходимо пополнить аккаунт на сумму от 5$.',
        reply_markup=get_payment_keyboard(p_case)
    )
