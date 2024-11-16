#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from datetime import date
from pydantic import BaseModel


class PayHistoryBase(BaseModel):

    """Class that defines instance attributes"""

    employeeNo: int
    payDate: date
    checkNumber: str
    payAmount: int


class PayHistoryCreate(PayHistoryBase):
    """Class that defines instance attributes"""

    pass


class PayHistory(PayHistoryBase):
    """Class that defines instance attributes"""

    payNo: int

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
