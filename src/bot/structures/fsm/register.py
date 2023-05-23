from aiogram.fsm.state import StatesGroup, State


class RegisterGroup(StatesGroup):
    confirmation = State()
    select = State()


class RegisterForSeller(StatesGroup):
    rules = State()
    add_tg_channel = State()


class RegisterForBuyer(StatesGroup):
    rules = State()
    fund = State()
