#!/usr/bin/python3
"""Module that defines tables"""

from .database import Base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date


class PurchaseOrder(Base):
    """Class that defines types of purchase orders"""

    __tablename__ = "orders"

    purchaseOrderNo = Column(Integer, primary_key=True, 
                        index=True, autoincrement=True)
    purchaseOrderDescription = Column(String, unique=True, index=True)
    orderDate = Column(DateTime, default=datetime.utcnow)
    dateRequired = Column(Date, nullable=False)
    shippedDate = Column(Date, nullable=False)
    freightCharge = Column(Integer, nullable=False)
    supplierNo = Column(Integer, ForeignKey("supplier.supplierNo"))
    employeeNo = Column(Integer, ForeignKey("employee.employeeNo"))

    supplier = relationship("Supplier", back_populates="order")
    employee = relationship("Employee", back_populates="order")


class Supplier(Base):
    """Class that defines a supplier"""

    __tablename__ = "supplier"

    supplierNo = Column(Integer, primary_key=True, 
                        index=True, autoincrement=True)
    supplierName = Column(String, unique=True, index=True)
    supplierCity = Column(String, unique=False)
    supplierState = Column(String, unique=False)
    supplierZipCode = Column(String, unique=False)
    suppTelNo = Column(String, unique=True, index=True)
    suppFaxNo = Column(String, unique=True, index=True)
    suppEmailAddress = Column(String, unique=True, index=True)
    suppWebAddress = Column(String, nullable=True)
    contactName = Column(String, nullable=True)
    contactTelNo = Column(String, nullable=True)
    contactFaxNo = Column(String, nullable=True)
    contactEmailAddress = Column(String, nullable=True)
    paymentTerms = Column(String, nullable=False)

    order = relationship("PurchaseOrder", back_populates="supplier")


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

    order = relationship("PurchaseOrder", back_populates="employee")
