#!/usr/bin/python3
"""Module that defines CRUD functions"""

from datetime import date
from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_bonuses_by_id(db: Session, employeeNo: int):
    """Function to return bonuses based on id"""

    return db.query(models.Bonus).filter(
            models.Bonus.employeeNo == employeeNo).all()


def get_bonuses_by_date(db: Session, bonusDate: date):
    """Function to return bonuses based on start date"""

    return db.query(models.Bonus).filter(
            models.Bonus.bonusDate == bonusDate).all()


def get_bonus(db: Session, employeeNo: int, bonusDate: date):
    """Function to return bonus based on start date"""

    return db.query(models.Bonus).filter(
            models.Bonus.employeeNo == employeeNo,
            models.Bonus.bonusDate == bonusDate).first()


def get_bonuses(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all bonuses"""

    return db.query(models.Bonus).offset(skip).limit(limit).all()


def create_bonus(db: Session, bonus: schemas.BonusCreate):
    """Function to create a bonus"""

    db_bonus = models.Bonus(employeeNo=bonus.employeeNo,
            bonusDate=bonus.bonusDate,
            bonusAmount=bonus.bonusAmount,
            bonusTypeNo=bonus.bonusTypeNo)
    db.add(db_bonus)
    db.commit()
    db.refresh(db_bonus)
    return db_bonus


def update_bonus(db: Session, employeeNo: int,
        bonusDate: date, bonus_update: schemas.BonusBase):
    """Function to update a bonus based on employeeNo and bonusDate"""

    db_bonus = db.query(Bonus).filter(Bonus.employeeNo == employeeNo,
            Bonus.bonusDate == bonusDate).first()
    if db_bonus:
        for key, value in bonus_update.dict().items():
            setattr(db_bonus, key, value)
        db.commit()
        db.refresh(db_bonus)
        return db_bonus
    else:
        raise HTTPException(status_code=404, detail="Bonus not found")


def delete_bonus(db: Session, employeeNo: int, bonusDate: date):
    """Function to delete a bonus based on employeeNo and bonusDate"""

    db_bonus = db.query(Bonus).filter(Bonus.employeeNo == employeeNo,
            Bonus.bonusDate == bonusDate).first()
    if db_bonus:
        db.delete(db_bonus)
        db.commit()
        return {"message": "Bonus deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Bonus not found")
