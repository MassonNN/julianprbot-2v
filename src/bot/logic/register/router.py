from aiogram import Router

from src.bot.filters.register_filter import RegisterFilter

register_router = Router(name='Register')
register_router.message.filter(RegisterFilter())
