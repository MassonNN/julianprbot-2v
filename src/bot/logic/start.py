""" This file represents a start logic """
from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from src.bot.filters.register_filter import RegisterFilter
from src.bot.structures.fsm.menu import MENU_KEYBOARD
from src.bot.structures.fsm.register import RegisterGroup
from src.bot.structures.keyboards.register import REGISTER_START_CONFIRM

start_router = Router(name="start")


@start_router.message(CommandStart(), RegisterFilter())
async def start_wo_register(message: types.Message, state: FSMContext):
    """Start command handler"""
    await state.set_state(RegisterGroup.confirmation)
    return await message.answer(
        'Привет! Это JulianPR, который поможет тебе в раскрутке или наоборот поможет '
        'заработать денег! Для того, чтобы начать регистрацию, нажми на кнопку внизу!',
        reply_markup=REGISTER_START_CONFIRM
    )


@start_router.message(CommandStart())
async def start_w_register(message: types.Message):
    """Start command handler"""
    return await message.answer(
        'Меню',
        reply_markup=MENU_KEYBOARD
    )
