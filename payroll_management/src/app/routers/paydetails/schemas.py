#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from datetime import date
from pydantic import BaseModel


class PayDetailBase(BaseModel):

    """Class that defines instance attributes"""

    employeeNo: int
    startDate: date
    routingNumber: int
    accountType: str
    bankName: str
    bankAddress: str
    payTypeNo: int


class PayDetailCreate(PayDetailBase):
    """Class that defines instance attributes"""

    pass


class PayDetail(PayDetailBase):
    """Class that defines instance attributes"""

    pass

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
