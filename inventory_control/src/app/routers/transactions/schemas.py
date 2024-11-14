#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from datetime import date
from pydantic import BaseModel


class TransactionBase(BaseModel):

    """Class that defines instance attributes"""

    transactionDescription: str
    unitPrice: int
    unitsOrdered: int
    unitsReceived: int
    unitsSold: int
    unitsWastage: int
    productNo: int
    purchaseOrderNo: int


class TransactionCreate(TransactionBase):
    """Class that defines instance attributes"""

    pass


class Transaction(TransactionBase):
    """Class that defines instance attributes"""

    transactionNo: int

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
