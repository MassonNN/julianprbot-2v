""" Channel model file """
import sqlalchemy as sa

from .base import Base


class ChannelPost(Base):
    """
    Associations M2M for Channel
    """
    channel_id = sa.ForeignKey('channel.id')
    post_id = sa.ForeignKey('post.id')
    
