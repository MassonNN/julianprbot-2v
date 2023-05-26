""" User repository file """

from sqlalchemy.ext.asyncio import AsyncSession

from .abstract import Repository
from ..models import Channel, Chat, Seller


class ChannelRepo(Repository[Channel]):
    """
    User repository for CRUD and other SQL queries
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize user repository as for all users or only for one user
        """
        super().__init__(type_model=Channel, session=session)

    async def new(
        self,
        chat: Chat,
        owner: Seller
    ) -> Channel:
        """
        Insert a new channel into the database
        """
        new_channel = await self.session.merge(
            Channel(
                chat=chat,
                owner=owner
            )
        )
        return new_channel
