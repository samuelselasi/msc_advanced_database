#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from pydantic import BaseModel


class BonusTypeBase(BaseModel):

    """Class that defines instance attributes"""

    bonusDescription: str


class BonusTypeCreate(BonusTypeBase):
    """Class that defines instance attributes"""

    pass


class BonusType(BonusTypeBase):
    """Class that defines instance attributes"""

    bonusTypeNo: int

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
