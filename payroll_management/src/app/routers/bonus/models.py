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

    bonus = relationship("Bonus", back_populates="employee")


class BonusType(Base):
    """Class that defines bonus types"""

    __tablename__ = "bonustype"

    bonusTypeNo = Column(Integer, primary_key=True, 
                        index=True, autoincrement=True)
    bonusDescription = Column(String, unique=True, index=True)

    bonus = relationship("Bonus", back_populates="bonustype")


class Bonus(Base):
    """Class that defines bonuses"""

    __tablename__ = "bonus"

    employeeNo = Column(Integer, ForeignKey("employee.employeeNo"))
    bonusDate = Column(Date, nullable=False, index=True)
    bonusAmount = Column(Integer, nullable=False)
    bonusTypeNo = Column(Integer, ForeignKey("bonustype.bonusTypeNo"))

    __table_args__ = (
        PrimaryKeyConstraint('employeeNo', 'bonusDate', name='pk_employee_bonusDate'),
    )

    employee = relationship("Employee", back_populates="bonus")
    bonustype = relationship("BonusType", back_populates="bonus")
