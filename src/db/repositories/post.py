""" Post repository file """

from sqlalchemy.ext.asyncio import AsyncSession

from .abstract import Repository
from ..models import User, Post, Channel
from ..types import Money


class PostRepo(Repository[Post]):
    """
    Post repository for CRUD and other SQL queries
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize user repository as for all users or only for one user
        """
        super().__init__(type_model=Post, session=session)

    async def new(
        self,
        text: str,
        budget: Money,
        url: str,
        author: User,
        channel: Channel
    ) -> Post:
        """
        Insert a new post into the database
        """
        new_post = await self.session.merge(
            Post(
                text=text,
                budget=budget,
                url=url,
                author=author,
                channel=channel
            )
        )
        return new_post
