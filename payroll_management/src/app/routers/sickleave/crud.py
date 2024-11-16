#!/usr/bin/python3
"""Module that defines CRUD functions"""

from datetime import date
from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_sickleaves_by_id(db: Session, employeeNo: int):
    """Function to return sick leave based on employee id"""

    return db.query(models.SickLeave).filter(
            models.SickLeave.employeeNo == employeeNo).all()


def get_sickleaves_by_date(db: Session, startDate: date):
    """Function to return sick leave based on start date"""

    return db.query(models.SickLeave).filter(
            models.SickLeave.startDate == startDate).all()


def get_sickleave(db: Session, employeeNo: int, startDate: date):
    """Function to return sick leave based on start date"""

    return db.query(models.SickLeave).filter(
            models.SickLeave.employeeNo == employeeNo,
            models.SickLeave.startDate == startDate).first()


def get_sickleaves(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all sick leaves"""

    return db.query(models.SickLeave).offset(skip).limit(limit).all()


def create_sickleave(db: Session, sickleave: schemas.SickLeaveCreate):
    """Function to create a sick leave"""

    db_sickleave = models.SickLeave(
            employeeNo=sickleave.employeeNo,
            startDate=sickleave.startDate,
            endDate=sickleave.endDate,
            reason=sickleave.reason)
    db.add(db_sickleave)
    db.commit()
    db.refresh(db_sickleave)
    return db_sickleave


def update_sickleave(db: Session, employeeNo: int,
        startDate: date, sickleave_update: schemas.SickLeaveBase):
    """Function to update a sick leave based on employeeNo and startDate"""

    db_sickleave = db.query(SickLeave).filter(
        SickLeave.employeeNo == employeeNo,
        SickLeave.startDate == startDate).first()
    if db_sickleave:
        for key, value in sickleave_update.dict().items():
            setattr(db_sickleave, key, value)
        db.commit()
        db.refresh(db_sickleave)
        return db_sickleave
    else:
        raise HTTPException(status_code=404, detail="Sick leave not found")


def delete_sickleave(db: Session, employeeNo: int, startDate: date):
    """Function to delete a sick leave based on employeeNo and startDate"""

    db_sickleave = db.query(SickLeave).filter(
            SickLeave.employeeNo == employeeNo,
            SickLeave.startDate == startDate).first()
    if db_sickleave:
        db.delete(db_sickleave)
        db.commit()
        return {"message": "Sick leave deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Sick leave not found")
