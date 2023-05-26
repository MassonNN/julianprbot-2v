import pytest
from aiogram import Dispatcher, Bot
from aiogram.methods import SendMessage

from src.bot.structures.keyboards.register import REGISTER_START_CONFIRM, REGISTER_SELECT_ROLE, REGISTER_RULES_READ
from tests.utils.updates import get_update, get_message, get_callback_query


@pytest.mark.asyncio
async def test_registration_for_buyer(dp: Dispatcher, bot: Bot):
    start_command = get_update(get_message('/start'))
    result = await dp.feed_update(bot, start_command)
    assert isinstance(result, SendMessage)
    assert result.text == ('Привет! Это JulianPR, который поможет тебе в раскрутке или наоборот поможет '
                           'заработать денег! Для того, чтобы начать регистрацию, нажми на кнопку внизу!')
    assert result.reply_markup == REGISTER_START_CONFIRM

    start_registration = get_update(get_message('Начать регистрацию'))
    result = await dp.feed_update(bot, start_registration)
    assert isinstance(result, SendMessage)
    assert result.text == 'Выбери тип своего профиля'
    assert result.reply_markup == REGISTER_SELECT_ROLE

    select_buyer_type = get_update(get_message('Я хочу покупать рекламу'))
    result = await dp.feed_update(bot, select_buyer_type)
    assert isinstance(result, SendMessage)
    assert result.text == 'Ознакомьтесь с нашими правилами'
    assert result.reply_markup == REGISTER_RULES_READ

    read_rules = get_update(callback_query=get_callback_query('read_rules'))
    result = await dp.feed_update(bot, read_rules)
    assert isinstance(result, SendMessage)
    assert result.text == 'Для продолжения регистрации необходимо пополнить аккаунт на сумму от 5$.'


@pytest.mark.asyncio
async def test_registration_for_seller(dp: Dispatcher, bot: Bot):
    start_command = get_update(get_message('/start'))
    result = await dp.feed_update(bot, start_command)
    assert isinstance(result, SendMessage)
    assert result.text == ('Привет! Это JulianPR, который поможет тебе в раскрутке или наоборот поможет '
                           'заработать денег! Для того, чтобы начать регистрацию, нажми на кнопку внизу!')
    assert result.reply_markup == REGISTER_START_CONFIRM

    start_registration = get_update(get_message('Начать регистрацию'))
    result = await dp.feed_update(bot, start_registration)
    assert isinstance(result, SendMessage)
    assert result.text == 'Выбери тип своего профиля'
    assert result.reply_markup == REGISTER_SELECT_ROLE

    select_buyer_type = get_update(get_message('Я владелец канала(ов) и хочу продавать рекламу'))
    result = await dp.feed_update(bot, select_buyer_type)
    assert isinstance(result, SendMessage)
    assert result.text == 'Ознакомьтесь с нашими правилами'
    assert result.reply_markup == REGISTER_RULES_READ

    read_rules = get_update(callback_query=get_callback_query('read_rules'))
    result = await dp.feed_update(bot, read_rules)
    assert isinstance(result, SendMessage)
    assert result.text.startswith('Для продолжения регистрации необходимо добавить хотя бы один телеграмм канал.')

    send_tg_channel = get_update(get_message('@test_channel'))
    result = await dp.feed_update(bot, send_tg_channel)
    assert isinstance(result, SendMessage)
    assert result.text.startswith('Твой канал отправлен в очередь на проверку модерацией!')
