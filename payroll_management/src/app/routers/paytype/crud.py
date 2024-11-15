#!/usr/bin/python3
"""Module that defines CRUD functions"""

from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_paytype_by_id(db: Session, payTypeNo: int):
    """Function to return pay type based on id"""

    return db.query(models.PayType).filter(models.PayType.payTypeNo == payTypeNo).first()


def get_paytype_by_name(db: Session, payDescription: str):
    """Function to return pay type based on name"""

    return db.query(models.PayType).filter(
            models.PayType.payDescription.ilike(f'%{payDescription}%')).first()


def get_paytypes(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all pay types"""

    return db.query(models.PayType).offset(skip).limit(limit).all()


def create_paytype(db: Session, paytype: schemas.PayTypeCreate):
    """Function to create a pay type"""

    db_paytype = models.PayType(payDescription=paytype.payDescription)
    db.add(db_paytype)
    db.commit()
    db.refresh(db_paytype)
    return db_paytype


def update_paytype(db: Session, payTypeNo: int,
        paytype_update: schemas.PayTypeBase):
    """Function to update a pay type based on its id"""

    db_paytype = get_paytype_by_id(db, payTypeNo=payTypeNo)
    if db_paytype:
        for key, value in paytype_update.dict().items():
            setattr(db_paytype, key, value)
        db.commit()
        db.refresh(db_paytype)
        return db_paytype
    else:
        raise HTTPException(status_code=404, detail="Pay type not found")


def delete_paytype(db: Session, payTypeNo: int):
    """Function to delete a pay type based on its id"""

    db_paytype = get_paytype_by_id(db, payTypeNo=payTypeNo)
    if db_paytype:
        db.delete(db_paytype)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Pay type not found")
