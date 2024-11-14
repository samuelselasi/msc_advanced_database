#!/usr/bin/python3
"""Module that defines CRUD functions"""

from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_bonustype_by_id(db: Session, bonusTypeNo: int):
    """Function to return bonus type based on id"""

    return db.query(models.BonusType).filter(models.BonusType.bonusTypeNo == bonusTypeNo).first()


def get_bonustype_by_name(db: Session, bonusDescription: str):
    """Function to return bonus type based on name"""

    return db.query(models.BonusType).filter(
            models.BonusType.bonusDescription.ilike(f'%{bonusDescription}%')).first()


def get_bonustypes(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all bonus types"""

    return db.query(models.BonusType).offset(skip).limit(limit).all()


def create_bonustype(db: Session, bonustype: schemas.BonusTypeCreate):
    """Function to create a bonus type"""

    db_bonustype = models.BonusType(bonusDescription=bonustype.bonusDescription)
    db.add(db_bonustype)
    db.commit()
    db.refresh(db_bonustype)
    return db_bonustype


def update_bonustype(db: Session, bonusTypeNo: int,
        bonustype_update: schemas.BonusTypeBase):
    """Function to update a bonus type based on its id"""

    db_bonustype = get_bonustype_by_id(db, bonusTypeNo=bonusTypeNo)
    if db_bonustype:
        for key, value in bonustype_update.dict().items():
            setattr(db_bonustype, key, value)
        db.commit()
        db.refresh(db_bonustype)
        return db_bonustype
    else:
        raise HTTPException(status_code=404, detail="Bonus type not found")


def delete_bonustype(db: Session, bonusTypeNo: int):
    """Function to delete a bonus type based on its id"""

    db_bonustype = get_bonustype_by_id(db, bonusTypeNo=bonusTypeNo)
    if db_bonustype:
        db.delete(db_bonustype)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Bonus type not found")
