#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from pydantic import BaseModel


class PayTypeBase(BaseModel):

    """Class that defines instance attributes"""

    payDescription: str


class PayTypeCreate(PayTypeBase):
    """Class that defines instance attributes"""

    pass


class PayType(PayTypeBase):
    """Class that defines instance attributes"""

    payTypeNo: int

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
