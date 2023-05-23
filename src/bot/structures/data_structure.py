"""
This file contains TypedDict structure to store data which will
transfer throw Dispatcher->Middlewares->Handlers
"""

from typing import Callable, TypedDict

from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.structures.role import Role
from src.cache import Cache
from src.db.database import Database


class TransferData(TypedDict):
    pool: Callable[[], AsyncSession]
    db: Database
    bot: Bot
    cache: Cache


class TransferUserData(TypedDict):
    role: Role
