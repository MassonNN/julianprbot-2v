""" Channel model file """
from typing import List

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .chat import Chat
from .base import Base
from .post import Post
from .seller import Seller


class Channel(Base):
    """
    Channel model
    """
    chat_fk = mapped_column(sa.ForeignKey('chat.id', ondelete='CASCADE'))
    chat = relationship(
        Chat,
        uselist=False,
        back_populates='channel',
        cascade='save-update,delete',
        lazy='joined'
    )
    owner_fk = mapped_column(sa.ForeignKey('seller.id', ondelete='SET NULL'))
    owner: Mapped[Seller] = relationship(
        uselist=False,
        back_populates='channels',
        cascade='save-update',
        lazy='joined'
    )
    posts: Mapped[List[Post]] = relationship(
        uselist=True,
        secondary='ChannelPost',
        cascade='save-update, delete, delete-orphan',
        lazy='selectin'
    )

