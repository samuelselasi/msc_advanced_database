#!/usr/bin/python3
"""Module that defines CRUD functions"""

from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_supplier_by_id(db: Session, supplierNo: int):
    """Function to return supplier based on id"""

    return db.query(models.Supplier).filter(models.Supplier.supplierNo == supplierNo).first()


def get_supplier_by_name(db: Session, supplierName: str):
    """Function to return supplier based on name"""

    return db.query(models.Supplier).filter(
            models.Supplier.supplierName.ilike(f'%{supplierName}%')).first()


def get_supplier_by_tel(db: Session, suppTelNo: str):
    """Function to return supplier based on telephone number"""

    return db.query(models.Supplier).filter(
            models.Supplier.suppTelNo.ilike(f'%{suppTelNo}%')).first()

def get_supplier_by_fax(db: Session, suppFaxNo: str):
    """Function to return supplier based on fax number"""

    return db.query(models.Supplier).filter(
            models.Supplier.suppFaxNo.ilike(f'%{suppFaxNo}%')).first()


def get_suppliers(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all suppliers"""

    return db.query(models.Supplier).offset(skip).limit(limit).all()


def create_supplier(db: Session, supplier: schemas.SupplierCreate):
    """Function to create a supplier"""

    db_supplier = models.Supplier(
            supplierName=supplier.supplierName,
            supplierCity=supplier.supplierCity,
            supplierState=supplier.supplierState,
            supplierZipCode=supplier.supplierZipCode,
            suppTelNo=supplier.suppTelNo,
            suppFaxNo=supplier.suppFaxNo,
            suppEmailAddress=supplier.suppEmailAddress,
            suppWebAddress=supplier.suppWebAddress,
            contactName=supplier.contactName,
            contactTelNo=supplier.contactTelNo,
            contactFaxNo=supplier.contactFaxNo,
            contactEmailAddress=supplier.contactEmailAddress,
            paymentTerms=supplier.paymentTerms)
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier


def update_supplier(db: Session, supplierNo: int,
                    supplier_update: schemas.SupplierBase):
    """Function to update a supplier based on its id"""

    db_supplier = get_supplier_by_id(db, supplierNo=supplierNo)
    if db_supplier:
        for key, value in supplier_update.dict().items():
            setattr(db_supplier, key, value)
        db.commit()
        db.refresh(db_supplier)
        return db_supplier
    else:
        raise HTTPException(status_code=404, detail="Supplier not found")


def delete_supplier(db: Session, supplierNo: int):
    """Function to delete a supplier based on its id"""

    db_supplier = get_supplier_by_id(db, supplierNo=supplierNo)
    if db_supplier:
        db.delete(db_supplier)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Supplier not found")
