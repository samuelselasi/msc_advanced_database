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


@router.get("/get_deductions", response_model=List[schemas.Deduct])
async def read_deductions(skip: int = 0, limit: int = 100,
                        db: Session = Depends(get_db)):
    """Endpoint to read all deductions"""

    deduct = crud.get_deductions(db, skip=skip, limit=limit)
    return deduct


@router.get("/get_deductions_by_no/{employeeNo}",
        response_model=List[schemas.Deduct])
async def read_deductions_no(employeeNo: int, db: Session = Depends(get_db)):
    """Endpoint to read deductions based on employee number"""

    db_deduct = crud.get_deductions_by_id(db, employeeNo=employeeNo)
    if db_deduct is None:
        raise HTTPException(status_code=404, detail="Deduction not found")
    return db_deduct


@router.get("/get_deduction/{employeeNo}/{deductDate}",
        response_model=schemas.Deduct)
async def get_deduction(
    employeeNo: int, deductDate: date, db: Session = Depends(get_db)):
    """Endpoint to get a deduction based on employeeNo and deductDate"""

    db_deduct = crud.get_deduction(db, employeeNo, deductDate)
    if db_deduct is None:
        raise HTTPException(status_code=404, detail="Deduction not found")
    return db_deduct


@router.get("/get_deductions_by_date", response_model=List[schemas.Deduct])
async def read_deductions_date(deductDate: str,
        db: Session = Depends(get_db)):
    """Endpoint to read deductions based on date"""

    db_deduct = crud.get_deductions_by_date(db, deductDate=deductDate)
    if db_deduct is None:
        raise HTTPException(status_code=404, detail="Deduction not found")
    return db_deduct


@router.post("/create_deduction", response_model=schemas.Deduct)
async def create_deduction(deduct: schemas.DeductCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a deduction"""

    db_deduct = db.query(models.Deduct).filter(
            models.Deduct.employeeNo == deduct.employeeNo,
            models.Deduct.deductDate == deduct.deductDate).first()
    if db_deduct:
        raise HTTPException(status_code=400,
                            detail="Deduction already exists for employee")
    return crud.create_deduction(db=db, deduct=deduct)


@router.put("/update_deduction/{employeeNo}/{deductDate}", 
        response_model=schemas.Deduct)
async def update_deduction(employeeNo: int, deductDate: date,
        deduct_update: schemas.DeductBase, db: Session = Depends(get_db)):
    """Endpoint to update a deduction based on employeeNo and deductDate"""

    return crud.update_deduction(db, employeeNo, deductDate, deduct_update)


@router.delete("/delete_deduction/{employeeNo}/{deductDate}",
        response_model=schemas.Deduct)
async def delete_deduction(employeeNo: int, deductDate: date,
        deduct_delete: schemas.DeductBase, db: Session = Depends(get_db)):
    """Endpoint to delete a deduction based on employeeNo and deductDate"""

    crud.delete_deduction(db, employeeNo, deductDate, deduct_delete)
    return {"message": "Deduction deleted successfully"}
