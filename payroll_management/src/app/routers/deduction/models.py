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

    deduct = relationship("Deduct", back_populates="employee")


class DeductType(Base):
    """Class that defines deduct types"""

    __tablename__ = "deducttype"

    deductTypeNo = Column(Integer, primary_key=True, 
                        index=True, autoincrement=True)
    deductDescription = Column(String, unique=True, index=True)

    deduct = relationship("Deduct", back_populates="deducttype")


class Deduct(Base):
    """Class that defines deductions"""

    __tablename__ = "deduct"

    employeeNo = Column(Integer, ForeignKey("employee.employeeNo"))
    deductDate = Column(Date, nullable=False, index=True)
    deductAmount = Column(Integer, nullable=False)
    deductTypeNo = Column(Integer, ForeignKey("deducttype.deductTypeNo"))

    __table_args__ = (
        PrimaryKeyConstraint('employeeNo', 'deductDate', name='pk_employee_deductDate'),
    )

    employee = relationship("Employee", back_populates="deduct")
    deducttype = relationship("DeductType", back_populates="deduct")
