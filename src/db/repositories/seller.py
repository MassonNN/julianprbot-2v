""" Seller repository file """

from sqlalchemy.ext.asyncio import AsyncSession

from .abstract import Repository
from ..models import User, Seller


class SellerRepo(Repository[Seller]):
    """
    Seller repository for CRUD and other SQL queries
    """

    def __init__(self, session: AsyncSession):
        super().__init__(type_model=Seller, session=session)

    async def new(
        self,
        tg_user: User
    ) -> None:
        """
        Insert a new seller into the database
        """
        new_seller = await self.session.merge(
            Seller(
              tg_user=tg_user
            )
        )
        return new_seller
