""" Roles """

import enum


class Role(enum.IntEnum):

    USER = 0
    MODERATOR = 1
    ADMINISTRATOR = 2


class ProfileType(enum.IntEnum):

    UNDEFINED = 0
    SELLER = 1
    BUYER = 2
