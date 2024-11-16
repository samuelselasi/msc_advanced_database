#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from datetime import date
from pydantic import BaseModel


class DeductBase(BaseModel):

    """Class that defines instance attributes"""

    employeeNo: int
    deductDate: date
    deductAmount: int
    deductTypeNo: int


class DeductCreate(DeductBase):
    """Class that defines instance attributes"""

    pass


class Deduct(DeductBase):
    """Class that defines instance attributes"""

    pass

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
