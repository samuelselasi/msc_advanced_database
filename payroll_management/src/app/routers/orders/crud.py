#!/usr/bin/python3
"""Module that defines CRUD functions"""

from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_order_by_id(db: Session, purchaseOrderNo: int):
    """Function to return purchase order based on id"""

    return db.query(models.PurchaseOrder).filter(models.PurchaseOrder.purchaseOrderNo == purchaseOrderNo).first()


def get_order_by_name(db: Session, purchaseOrderDescription: str):
    """Function to return purchase order based on name"""

    return db.query(models.PurchaseOrder).filter(
            models.PurchaseOrder.purchaseOrderDescription.ilike(f'%{purchaseOrderDescription}%')).first()


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all purchase orders"""

    return db.query(models.PurchaseOrder).offset(skip).limit(limit).all()


def create_order(db: Session, order: schemas.OrderCreate):
    """Function to create an order"""

    db_order = models.PurchaseOrder(
            purchaseOrderDescription=order.purchaseOrderDescription,
            dateRequired=order.dateRequired,
            shippedDate=order.shippedDate,
            freightCharge=order.freightCharge,
            supplierNo=order.supplierNo,
            employeeNo=order.employeeNo)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def update_order(db: Session, purchaseOrderNo: int,
                    order_update: schemas.OrderBase):
    """Function to update a purchase order based on its id"""

    db_order = get_order_by_id(db, purchaseOrderNo=purchaseOrderNo)
    if db_order:
        for key, value in order_update.dict().items():
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
        return db_order
    else:
        raise HTTPException(
                status_code=404, detail="Purchase order not found")


def delete_order(db: Session, purchaseOrderNo: int):
    """Function to delete a purchase order based on its id"""

    db_order = get_order_by_id(db, purchaseOrderNo=purchaseOrderNo)
    if db_order:
        db.delete(db_order)
        db.commit()
    else:
        raise HTTPException(
                status_code=404, detail="Purchase order not found")
