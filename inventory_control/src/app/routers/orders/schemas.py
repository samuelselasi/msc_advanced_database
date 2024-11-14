#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from datetime import date
from pydantic import BaseModel


class OrderBase(BaseModel):

    """Class that defines instance attributes"""

    purchaseOrderDescription: str
    # orderDate: date
    dateRequired: date
    shippedDate: date
    freightCharge: int
    supplierNo: int
    employeeNo: int


class OrderCreate(OrderBase):
    """Class that defines instance attributes"""

    pass


class Order(OrderBase):
    """Class that defines instance attributes"""

    purchaseOrderNo: int

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
