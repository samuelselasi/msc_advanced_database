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

    paydetail = relationship("PayDetail", back_populates="employee")


class PayType(Base):
    """Class that defines pay types"""

    __tablename__ = "paytype"

    payTypeNo = Column(Integer, primary_key=True, 
                        index=True, autoincrement=True)
    payDescription = Column(String, unique=True, index=True)

    paydetail = relationship("PayDetail", back_populates="paytype")


class PayDetail(Base):
    """Class that defines pay details"""

    __tablename__ = "paydetail"

    employeeNo = Column(Integer, ForeignKey("employee.employeeNo"))
    startDate = Column(Date, nullable=False, index=True)
    routingNumber = Column(Integer, nullable=False, unique=True)
    accountType = Column(String, nullable=False)
    bankName = Column(String, nullable=False)
    bankAddress = Column(String, nullable=False)
    payTypeNo = Column(Integer, ForeignKey("paytype.payTypeNo"))

    __table_args__ = (
        PrimaryKeyConstraint('employeeNo', 'startDate', name='pk_employee_startDate3'),
    )

    employee = relationship("Employee", back_populates="paydetail")
    paytype = relationship("PayType", back_populates="paydetail")
