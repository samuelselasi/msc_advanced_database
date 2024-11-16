#!/usr/bin/python3
"""Module that defines CRUD functions"""

from datetime import date
from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_deductions_by_id(db: Session, employeeNo: int):
    """Function to return deductions based on id"""

    return db.query(models.Deduct).filter(
            models.Deduct.employeeNo == employeeNo).all()


def get_deductions_by_date(db: Session, deductDate: date):
    """Function to return deductions based on date"""

    return db.query(models.Deduct).filter(
            models.Deduct.deductDate == deductDate).all()


def get_deduction(db: Session, employeeNo: int, deductDate: date):
    """Function to return deduction based on date"""

    return db.query(models.Deduct).filter(
            models.Deduct.employeeNo == employeeNo,
            models.Deduct.deductDate == deductDate).first()


def get_deductions(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all deductions"""

    return db.query(models.Deduct).offset(skip).limit(limit).all()


def create_deduction(db: Session, deduct: schemas.DeductCreate):
    """Function to create a deduction"""

    db_deduct = models.Deduct(employeeNo=deduct.employeeNo,
            deductDate=deduct.deductDate,
            deductAmount=deduct.deductAmount,
            deductTypeNo=deduct.deductTypeNo)
    db.add(db_deduct)
    db.commit()
    db.refresh(db_deduct)
    return db_deduct


def update_deduction(db: Session, employeeNo: int,
        deductDate: date, deduct_update: schemas.DeductBase):
    """Function to update a deduction based on employeeNo and deductDate"""

    db_deduct = db.query(Deduct).filter(Deduct.employeeNo == employeeNo,
            Deduct.deductDate == deductDate).first()
    if db_deduct:
        for key, value in deduct_update.dict().items():
            setattr(db_deduct, key, value)
        db.commit()
        db.refresh(db_deduct)
        return db_deduct
    else:
        raise HTTPException(status_code=404, detail="Deduction not found")


def delete_deduction(db: Session, employeeNo: int, deductDate: date):
    """Function to delete a deduction based on employeeNo and deductDate"""

    db_deduct = db.query(Deduct).filter(Deduct.employeeNo == employeeNo,
            Deduct.deductDate == deductDate).first()
    if db_deduct:
        db.delete(db_deduct)
        db.commit()
        return {"message": "Deduction deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Deduction not found")
