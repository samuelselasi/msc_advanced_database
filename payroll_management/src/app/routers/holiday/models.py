#!/usr/bin/python3
"""Module that defines tables"""

from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date


class Employee(Base):
    """Class that defines an employee"""

    __tablename__ = "employee"

    employeeNo = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)
    employeeName = Column(String, unique=True, index=True)
    employeeCity = Column(String, unique=False)
    employeeState = Column(String, unique=False)
    employeeZipCode = Column(String, unique=False)
    employeeTelNo = Column(String, unique=True, index=True)
    employeeFaxNo = Column(String, unique=True, index=True)
    employeeEmailAddress = Column(String, unique=True, index=True)

    holiday = relationship("Holiday", back_populates="employee")


class Holiday(Base):
    """Class that defines holidays"""

    __tablename__ = "holiday"

    employeeNo = Column(Integer, ForeignKey("employee.employeeNo"))
    startDate = Column(Date, nullable=False, index=True)
    endDate = Column(Date, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('employeeNo', 'startDate', name='pk_employee_startDate'),
    )

    employee = relationship("Employee", back_populates="holiday")
