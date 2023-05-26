from typing import Callable

import pytest
import pytest_asyncio
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.dispatcher import get_dispatcher
from src.bot.structures.data_structure import TransferData
from src.cache import Cache
from src.db.database import create_session_maker
from tests.utils.mocked_bot import MockedBot
from tests.utils.mocked_database import MockedDatabase
from tests.utils.mocked_redis import MockedRedis


@pytest_asyncio.fixture()
async def pool():
    pool = create_session_maker()
    yield pool
    await pool.close_all()  # noqa


@pytest_asyncio.fixture()
async def db(pool: Callable[[], AsyncSession]):
    session = pool()
    database = MockedDatabase(session)
    yield database
    await database.teardown()
    await session.close()


@pytest.fixture()
def bot():
    return MockedBot()


@pytest.fixture()
def storage():
    return MemoryStorage()


@pytest.fixture()
def dp(storage):
    return get_dispatcher(storage=storage)


@pytest.fixture()
def cache():
    return Cache(redis=MockedRedis())


@pytest.fixture()
def transfer_data(pool, db, bot, cache):
    return TransferData(
        pool=pool,
        db=db,
        cache=cache
    )
