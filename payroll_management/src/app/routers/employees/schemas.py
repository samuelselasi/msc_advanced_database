#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from pydantic import BaseModel


class EmployeeBase(BaseModel):

    """Class that defines instance attributes"""

    employeeName: str
    employeeCity: str
    employeeState: str
    employeeZipCode: str
    employeeTelNo: str
    employeeFaxNo: str
    employeeEmailAddress: str


class EmployeeCreate(EmployeeBase):
    """Class that defines instance attributes"""

    pass


class Employee(EmployeeBase):
    """Class that defines instance attributes"""

    employeeNo: int

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
