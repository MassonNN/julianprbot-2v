""" Buyer repository file """

from sqlalchemy.ext.asyncio import AsyncSession

from .abstract import Repository
from ..models import User, Buyer


class BuyerRepo(Repository[Buyer]):
    """
    Buyer repository for CRUD and other SQL queries
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize user repository as for all users or only for one user
        """
        super().__init__(type_model=Buyer, session=session)

    async def new(
        self,
        tg_user: User
    ) -> Buyer:
        """
        Insert a new user into the database
        :param tg_user: Telegram chat with user
        """
        new_buyer = await self.session.merge(
            Buyer(
                tg_user=tg_user
            )
        )
        return new_buyer
