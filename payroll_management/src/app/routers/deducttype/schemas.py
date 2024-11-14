#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from pydantic import BaseModel


class DeductTypeBase(BaseModel):

    """Class that defines instance attributes"""

    deductDescription: str


class DeductTypeCreate(DeductTypeBase):
    """Class that defines instance attributes"""

    pass


class DeductType(DeductTypeBase):
    """Class that defines instance attributes"""

    deductTypeNo: int

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
