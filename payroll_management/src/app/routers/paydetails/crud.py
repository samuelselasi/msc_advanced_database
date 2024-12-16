#!/usr/bin/python3
"""Module that defines CRUD functions"""

from datetime import date
from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_paydetails_by_id(db: Session, employeeNo: int):
    """Function to return pay details based on id"""

    return db.query(models.PayDetail).filter(
            models.PayDetail.employeeNo == employeeNo).all()


def get_paydetails_by_date(db: Session, startDate: date):
    """Function to return pay details based on start date"""

    return db.query(models.PayDetail).filter(
            models.PayDetail.startDate == startDate).all()


def get_paydetail(db: Session, employeeNo: int, startDate: date):
    """Function to return pay deatil based on start date"""

    return db.query(models.PayDetail).filter(
            models.PayDetail.employeeNo == employeeNo,
            models.PayDetail.startDate == startDate).first()


def get_paydetails(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all pay details"""

    return db.query(models.PayDetail).offset(skip).limit(limit).all()


def create_paydetail(db: Session, paydetail: schemas.PayDetailCreate):
    """Function to create a pay detail"""

    db_paydetail = models.PayDetail(employeeNo=paydetail.employeeNo,
            startDate=paydetail.startDate,
            routingNumber=paydetail.routingNumber,
            accountType=paydetails.accountType,
            bankName=paydetails.bankName,
            bankAddress=paydetails.bankAddress,
            payTypeNo=paydetails.payTypeNo)
    db.add(db_paydetail)
    db.commit()
    db.refresh(db_paydetail)
    return db_paydetail


def update_paydetail(db: Session, employeeNo: int,
        startDate: date, paydetail_update: schemas.PayDetailBase):
    """Function to update a pay detail based on employeeNo and startDate"""

    db_paydetail = db.query(PayDetail).filter(
            PayDetail.employeeNo == employeeNo,
            PayDetail.startDate == startDate).first()
    if db_paydetail:
        for key, value in paydetail_update.dict().items():
            setattr(db_paydetail, key, value)
        db.commit()
        db.refresh(db_paydetail)
        return db_paydetail
    else:
        raise HTTPException(status_code=404, detail="Pay detail not found")


def delete_paydetail(db: Session, employeeNo: int, startDate: date):
    """Function to delete a pay detail based on employeeNo and startDate"""

    db_paydetail = db.query(PayDetail).filter(
            PayDetail.employeeNo == employeeNo,
            PayDetail.startDate == startDate).first()
    if db_paydetail:
        db.delete(db_paydetail)
        db.commit()
        return {"message": "Pay detail deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Pay detail not found")
