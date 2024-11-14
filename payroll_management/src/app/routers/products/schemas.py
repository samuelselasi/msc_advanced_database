#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from pydantic import BaseModel


class ProductBase(BaseModel):

    """Class that defines instance attributes"""

    productName: str
    serialNo: str
    unitPrice: int
    quantityOnHand: int
    reorderLevel: int
    reorderQuantity: int
    reorderLeadTime: int
    categoryNo: int


class ProductCreate(ProductBase):
    """Class that defines instance attributes"""

    pass


class Product(ProductBase):
    """Class that defines instance attributes"""

    productNo: int

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
