#!/usr/bin/python3
"""Module that defines CRUD functions"""

from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_deducttype_by_id(db: Session, deductTypeNo: int):
    """Function to return deduct type based on id"""

    return db.query(models.DeductType).filter(models.DeductType.deductTypeNo == deductTypeNo).first()


def get_deducttype_by_name(db: Session, deductDescription: str):
    """Function to return deduct type based on name"""

    return db.query(models.DeductType).filter(
            models.DeductType.deductDescription.ilike(f'%{deductDescription}%')).first()


def get_deducttypes(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all deduct types"""

    return db.query(models.DeductType).offset(skip).limit(limit).all()


def create_deducttype(db: Session, deducttype: schemas.DeductTypeCreate):
    """Function to create a deduct type"""

    db_deducttype = models.DeductType(deductDescription=deducttype.deductDescription)
    db.add(db_deducttype)
    db.commit()
    db.refresh(db_deducttype)
    return db_deducttype


def update_deducttype(db: Session, deductTypeNo: int,
        deducttype_update: schemas.DeductTypeBase):
    """Function to update a deduct type based on its id"""

    db_deducttype = get_deducttype_by_id(db, deductTypeNo=deductTypeNo)
    if db_deducttype:
        for key, value in deducttype_update.dict().items():
            setattr(db_deducttype, key, value)
        db.commit()
        db.refresh(db_deducttype)
        return db_deducttype
    else:
        raise HTTPException(status_code=404, detail="Deduct type not found")


def delete_deducttype(db: Session, deductTypeNo: int):
    """Function to delete a deduct type based on its id"""

    db_deducttype = get_deducttype_by_id(db, deductTypeNo=deductTypeNo)
    if db_deducttype:
        db.delete(db_deducttype)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Deduct type not found")
