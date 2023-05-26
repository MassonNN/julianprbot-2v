""" Post model file """

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .buyer import Buyer
from ..types import Money


class Post(Base):
    """
    Post model
    """
    text: Mapped[str]
    budget: Mapped[Money]  # TODO: change type if needed
    url: Mapped[str]

    author_fk = mapped_column(sa.ForeignKey('buyer.id', ondelete='SET NULL'))
    author: Mapped[Buyer] = relationship(uselist=False, back_populates='posts')
    channel = relationship("Channel", secondary="ChannelPost", uselist=True)
