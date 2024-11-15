#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from datetime import date
from pydantic import BaseModel


class HolidayBase(BaseModel):

    """Class that defines instance attributes"""

    employeeNo: int
    startDate: date
    endDate: date


class HolidayCreate(HolidayBase):
    """Class that defines instance attributes"""

    pass


class Holiday(HolidayBase):
    """Class that defines instance attributes"""

    pass

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
