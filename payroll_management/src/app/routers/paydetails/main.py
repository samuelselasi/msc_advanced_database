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


@router.get("/get_paydetails", response_model=List[schemas.PayDetail])
async def read_paydetails(skip: int = 0, limit: int = 100,
        db: Session = Depends(get_db)):
    """Endpoint to read all pay details"""

    details = crud.get_paydetails(db, skip=skip, limit=limit)
    return details


@router.get("/get_paydetails_by_no/{employeeNo}",
        response_model=List[schemas.PayDetail])
async def read_paydetails_no(employeeNo: int, db: Session = Depends(get_db)):
    """Endpoint to read pay details based on employee number"""

    db_pay = crud.get_paydetails_by_id(db, employeeNo=employeeNo)
    if db_pay is None:
        raise HTTPException(status_code=404, detail="Pay details not found")
    return db_pay


@router.get("/get_paydetail/{employeeNo}/{startDate}",
        response_model=schemas.PayDetail)
async def get_paydetail(
    employeeNo: int, startDate: date, db: Session = Depends(get_db)):
    """Endpoint to get a pay detail based on employeeNo and startDate"""

    db_pay = crud.get_paydetail(db, employeeNo, startDate)
    if db_pay is None:
        raise HTTPException(status_code=404, detail="Pay detail not found")
    return db_pay


@router.get("/get_paydetails_by_date", response_model=List[schemas.PayDetail])
async def read_paydetails_date(startDate: str, db: Session = Depends(get_db)):
    """Endpoint to read pay details based on date"""

    db_pay = crud.get_paydetails_by_date(db, startDate=startDate)
    if db_pay is None:
        raise HTTPException(status_code=404, detail="Pay details not found")
    return db_pay


@router.post("/create_paydetail", response_model=schemas.PayDetail)
async def create_paydetail(paydetail: schemas.PayDetailCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a pay detail"""

    db_pay = db.query(models.PayDetail).filter(
            models.PayDetail.employeeNo == paydetail.employeeNo,
            models.PayDetail.startDate == paydetail.startDate).first()
    if db_pay:
        raise HTTPException(status_code=400,
                            detail="Pay detail already exists for employee")
    return crud.create_paydetail(db=db, paydetail=paydetail)


@router.put("/update_paydetail/{employeeNo}/{startDate}", 
        response_model=schemas.PayDetail)
async def update_paydetail(employeeNo: int, startDate: date,
        paydetail_update: schemas.PayDetailBase,
        db: Session = Depends(get_db)):
    """Endpoint to update a pay detail based on employeeNo and startDate"""

    return crud.update_paydetail(db, employeeNo, startDate, paydetail_update)


@router.delete("/delete_paydetail/{employeeNo}/{startDate}",
        response_model=None)
async def delete_paydetail(employeeNo: int, startDate: date,
        paydetail_delete: schemas.PayDetailBase,
        db: Session = Depends(get_db)):
    """Endpoint to delete a pay detail based on employeeNo and startDate"""

    crud.delete_paydetail(db, employeeNo, startDate, paydetail_delete)
    return {"message": "Pay detail deleted successfully"}
