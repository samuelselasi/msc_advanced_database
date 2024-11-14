#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from pydantic import BaseModel


class CategoryBase(BaseModel):

    """Class that defines instance attributes"""

    categoryDescription: str


class CategoryCreate(CategoryBase):
    """Class that defines instance attributes"""

    pass


class ProductCategory(CategoryBase):
    """Class that defines instance attributes"""

    categoryNo: int

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
