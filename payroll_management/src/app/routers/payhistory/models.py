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

    payhistory = relationship("PayHistory", back_populates="employee")


class PayHistory(Base):
    """Class that defines pay history"""

    __tablename__ = "payhistory"

    payNo = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)
    employeeNo = Column(Integer, ForeignKey("employee.employeeNo"))
    payDate = Column(Date, nullable=False, index=True)
    checkNumber = Column(String, nullable=False, unique=False)
    payAmount = Column(Integer, nullable=False)

    employee = relationship("Employee", back_populates="payhistory")
