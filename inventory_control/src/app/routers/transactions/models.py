#!/usr/bin/python3
"""Module that defines tables"""

from .database import Base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date


class Transaction(Base):
    """Class that defines transactions"""

    __tablename__ = "transactions"

    transactionNo = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)
    transactionDate = Column(DateTime, default=datetime.utcnow)
    transactionDescription = Column(String, unique=True, index=True)
    unitPrice = Column( Integer, nullable=False)
    unitsOrdered = Column(Integer, nullable=False)
    unitsReceived = Column(Integer, nullable=False)
    unitsSold = Column(Integer, nullable=False)
    unitsWastage = Column(Integer, nullable=False)
    productNo = Column(Integer, ForeignKey("products.productNo"))
    purchaseOrderNo = Column(Integer, ForeignKey("orders.purchaseOrderNo"))

    product = relationship("Product", back_populates="transaction")
    order = relationship("PurchaseOrder", back_populates="transaction")


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
    transaction = relationship("Transaction", back_populates="order")


class ProductCategory(Base):
    """Class that defines types of product categories"""

    __tablename__ = "category"

    categoryNo = Column(Integer, primary_key=True, 
                        index=True, autoincrement=True)
    categoryDescription = Column(String, unique=True, index=True)

    product = relationship("Product", back_populates="category")


class Product(Base):
    """Class that defines types of product categories"""

    __tablename__ = "products"

    productNo = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)
    productName = Column(String, unique=True, index=True)
    serialNo = Column(String, unique=True, index=True)
    unitPrice = Column(Integer, nullable=False)
    quantityOnHand = Column(Integer, nullable=False)
    reorderLevel = Column(Integer, nullable=False)
    reorderQuantity = Column(Integer, nullable=False)
    reorderLeadTime = Column(Integer, nullable=False)
    categoryNo = Column(Integer, ForeignKey("category.categoryNo"))

    category = relationship("ProductCategory", back_populates="product")
    transaction = relationship("Transaction", back_populates="product")


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
