#!/usr/bin/python3
"""Module that defines CRUD functions"""

from datetime import date
from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_payhistory_by_id(db: Session, payNo: int):
    """Function to return pay history based on id"""

    return db.query(models.PayHistory).filter(
            models.PayHistory.payNo == payNo).first()


def get_payhistory_by_emp(db: Session, employeeNo: int):
    """Function to return pay history based on employee id"""

    return db.query(models.PayHistory).filter(
            models.PayHistory.employeeNo == employeeNo).all()


def get_payhistories(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all pay histories"""

    return db.query(models.PayHistory).offset(skip).limit(limit).all()


def create_payhistory(db: Session, payhistory: schemas.PayHistoryCreate):
    """Function to create a pay history"""

    db_payhistory = models.Holiday(
            employeeNo=payhistory.employeeNo,
            payDate=payhistory.payDate,
            checkNumber=payhistory.checkNumber,
            payAmount=payhistory.payAmount)
    db.add(db_payhistory)
    db.commit()
    db.refresh(db_payhistory)
    return db_payhistory


def update_payhistory(db: Session, payNo: int,
        payhistory_update: schemas.PayHistoryBase):
    """Function to update a pay history based on id"""

    db_payhistory = db.query(PayHistory).filter(
            PayHistory.payNo == payNo).first()

    if db_payhistory:
        for key, value in payhistory_update.dict().items():
            setattr(db_payhistory, key, value)
        db.commit()
        db.refresh(db_payhistory)
        return db_payhistory
    else:
        raise HTTPException(status_code=404, detail="Pay history not found")


def delete_payhistory(db: Session, payNo: int):
    """Function to delete a pay history based on id"""

    db_payhistory = db.query(PayHistory).filter(
            PayHistory.payNo == payNo).first()

    if db_payhistory:
        db.delete(db_payhistory)
        db.commit()
        return {"message": "Pay history deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Pay history not found")
