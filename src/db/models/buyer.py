""" Buyer model file """
from typing import List

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .user import User
from .base import Base
from ..types import Money


class Buyer(Base):
    """
    Buyer model
    """
    balance: Mapped[Money]  # TODO: change type if needed

    tg_user_fk = mapped_column(sa.ForeignKey('user.id', cascade='SET NULL'))
    tg_user: Mapped[User] = relationship(uselist=False, lazy='joined', cascade='save-update')
    posts = relationship(
        'Post',
        back_populates='author',
        lazy='selectin',
        cascade='save-update,delete'
    )
