#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from datetime import date
from pydantic import BaseModel


class BonusBase(BaseModel):

    """Class that defines instance attributes"""

    employeeNo: int
    bonusDate: date
    bonusAmount: int
    bonusTypeNo: int


class BonusCreate(BonusBase):
    """Class that defines instance attributes"""

    pass


class Bonus(BonusBase):
    """Class that defines instance attributes"""

    pass

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
