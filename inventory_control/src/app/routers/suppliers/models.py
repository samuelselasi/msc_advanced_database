#!/usr/bin/python3
"""Module that defines tables"""

from .database import Base
from sqlalchemy import Column, Integer, String


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
