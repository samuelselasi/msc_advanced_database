#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from datetime import date
from pydantic import BaseModel


class SickLeaveBase(BaseModel):

    """Class that defines instance attributes"""

    employeeNo: int
    startDate: date
    endDate: date
    reason: str


class SickLeaveCreate(SickLeaveBase):
    """Class that defines instance attributes"""

    pass


class SickLeave(SickLeaveBase):
    """Class that defines instance attributes"""

    pass

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
