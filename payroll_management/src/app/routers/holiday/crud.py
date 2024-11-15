#!/usr/bin/python3
"""Module that defines CRUD functions"""

from datetime import date
from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_holidays_by_id(db: Session, employeeNo: int):
    """Function to return holiday based on id"""

    return db.query(models.Holiday).filter(
            models.Holiday.employeeNo == employeeNo).all()


def get_holidays_by_date(db: Session, startDate: date):
    """Function to return holiday based on start date"""

    return db.query(models.Holiday).filter(
            models.Holiday.startDate == startDate).all()


def get_holiday(db: Session, employeeNo: int, startDate: date):
    """Function to return holiday based on start date"""

    return db.query(models.Holiday).filter(
            models.Holiday.employeeNo == employeeNo,
            models.Holiday.startDate == startDate).first()


def get_holidays(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all holidays"""

    return db.query(models.Holiday).offset(skip).limit(limit).all()


def create_holiday(db: Session, holiday: schemas.HolidayCreate):
    """Function to create a holiday"""

    db_holiday = models.Holiday(
            employeeNo=holiday.employeeNo,
            startDate=holiday.startDate,
            endDate=holiday.endDate)
    db.add(db_holiday)
    db.commit()
    db.refresh(db_holiday)
    return db_holiday


def update_holiday(db: Session, employeeNo: int,
        startDate: date, holiday_update: schemas.HolidayBase):
    """Function to update a holiday based on employeeNo and startDate"""

    db_holiday = db.query(Holiday).filter(
        Holiday.employeeNo == employeeNo,
        Holiday.startDate == startDate).first()

    if db_holiday:
        for key, value in holiday_update.dict().items():
            setattr(db_holiday, key, value)
        db.commit()
        db.refresh(db_holiday)
        return db_holiday
    else:
        raise HTTPException(status_code=404, detail="Holiday not found")


def delete_holiday(db: Session, employeeNo: int, startDate: date):
    """Function to delete a holiday based on employeeNo and startDate"""

    db_holiday = db.query(Holiday).filter(
            Holiday.employeeNo == employeeNo,
            Holiday.startDate == startDate).first()

    if db_holiday:
        db.delete(db_holiday)
        db.commit()
        return {"message": "Holiday deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Holiday not found")
