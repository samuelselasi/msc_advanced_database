#!/usr/bin/python3
"""Module that defines orm schemas for tables"""

from pydantic import BaseModel


class SupplierBase(BaseModel):

    """Class that defines instance attributes"""

    supplierName: str
    supplierCity: str
    supplierState: str
    supplierZipCode: str
    suppTelNo: str
    suppFaxNo: str
    suppEmailAddress: str
    suppWebAddress: str
    contactName: str
    contactTelNo: str
    contactFaxNo: str
    contactEmailAddress: str
    paymentTerms: str


class SupplierCreate(SupplierBase):
    """Class that defines instance attributes"""

    pass


class Supplier(SupplierBase):
    """Class that defines instance attributes"""

    supplierNo: int

    class Config:
        """Class that configures ORM mode"""

        from_attributes = True
