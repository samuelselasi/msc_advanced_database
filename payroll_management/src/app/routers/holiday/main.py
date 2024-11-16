#!/usr/bin/python3
"""Module that defines endpoints functions"""

from typing import List
from datetime import date
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi import Depends, HTTPException, APIRouter

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/get_holidays", response_model=List[schemas.Holiday])
async def read_holidays(skip: int = 0, limit: int = 100,
                        db: Session = Depends(get_db)):
    """Endpoint to read all holidays"""

    holidays = crud.get_holidays(db, skip=skip, limit=limit)
    return holidays


@router.get("/get_holiday_by_no/{employeeNo}", response_model=List[schemas.Holiday])
async def read_holiday_no(employeeNo: int, db: Session = Depends(get_db)):
    """Endpoint to read holiday based on its number"""

    db_holiday = crud.get_holidays_by_id(db, employeeNo=employeeNo)
    if db_holiday is None:
        raise HTTPException(status_code=404, detail="Holiday not found")
    return db_holiday


@router.get("/get_holiday/{employeeNo}/{startDate}",
        response_model=schemas.Holiday)
async def get_holiday(
    employeeNo: int, startDate: date, db: Session = Depends(get_db)):
    """Endpoint to get a holiday based on employeeNo and startDate"""

    db_holiday = crud.get_holiday(db, employeeNo, startDate)
    if db_holiday is None:
        raise HTTPException(status_code=404, detail="Holiday not found")
    return db_holiday


@router.get("/get_holiday_by_date", response_model=List[schemas.Holiday])
async def read_holidays_date(startDate: str, db: Session = Depends(get_db)):
    """Endpoint to read holiday based on start date"""

    db_holiday = crud.get_holidays_by_date(db, startDate=startDate)
    if db_holiday is None:
        raise HTTPException(status_code=404, detail="Holiday not found")
    return db_holiday


@router.post("/create_holiday", response_model=schemas.Holiday)
async def create_holiday(holiday: schemas.HolidayCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a holiday"""

    db_holiday = db.query(models.Holiday).filter(
            models.Holiday.employeeNo == holiday.employeeNo,
            models.Holiday.startDate == holiday.startDate).first()
    if db_holiday:
        raise HTTPException(status_code=400,
                            detail="Holiday already exists for employee")
    return crud.create_holiday(db=db, holiday=holiday)


@router.put("/update_holiday/{employeeNo}/{startDate}", 
        response_model=schemas.Holiday)
async def update_holiday(
        employeeNo: int, startDate: date, holiday_update: schemas.HolidayBase,
        db: Session = Depends(get_db)):
    """Endpoint to update a holiday based on employeeNo and startDate"""

    return crud.update_holiday(db, employeeNo, startDate, holiday_update)


@router.delete("/delete_holiday/{employeeNo}/{startDate}",
        response_model=schemas.Holiday)
async def delete_holiday(
        employeeNo: int, startDate: date, holiday_delete: schemas.HolidayBase,
        db: Session = Depends(get_db)):
    """Endpoint to delete a holiday based on employeeNo and startDate"""

    crud.delete_holiday(db, employeeNo, startDate, holiday_delete)
    return {"message": "Product deleted successfully"}
