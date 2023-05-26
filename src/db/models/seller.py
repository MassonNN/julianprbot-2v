""" Seller model file """
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .user import User
from .base import Base


class Seller(Base):
    """
    Seller model
    """
    balance: Mapped[float]  # TOOD: change type if needed

    tg_user_fk = mapped_column(sa.ForeignKey('user.id'))
    tg_user: Mapped[User] = relationship(uselist=False, lazy='joined')
    channels = relationship("Channel", uselist=True, lazy='selectin')
