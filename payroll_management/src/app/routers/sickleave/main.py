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


@router.get("/get_sickleaves", response_model=List[schemas.SickLeave])
async def read_sickleaves(skip: int = 0, limit: int = 100,
                        db: Session = Depends(get_db)):
    """Endpoint to read all sick leaves"""

    sickleaves = crud.get_sickleaves(db, skip=skip, limit=limit)
    return sickleaves


@router.get("/get_sickleave_by_no/{employeeNo}", 
        response_model=List[schemas.SickLeave])
async def read_sickleave_no(employeeNo: int, db: Session = Depends(get_db)):
    """Endpoint to read sick leaves based on employee number"""

    db_sickleave = crud.get_sickleaves_by_id(db, employeeNo=employeeNo)
    if db_sickleave is None:
        raise HTTPException(status_code=404, detail="Sickleave not found")
    return db_sickleave


@router.get("/get_sickleave/{employeeNo}/{startDate}",
        response_model=schemas.SickLeave)
async def get_sickleave(
    employeeNo: int, startDate: date, db: Session = Depends(get_db)):
    """Endpoint to get a sick leave based on employeeNo and startDate"""

    db_sickleave = crud.get_sickleave(db, employeeNo, startDate)
    if db_sickleave is None:
        raise HTTPException(status_code=404, detail="Sick leave not found")
    return db_sickleave


@router.get("/get_sickleaves_by_date", response_model=List[schemas.SickLeave])
async def read_sickleaves_date(startDate: str, db: Session = Depends(get_db)):
    """Endpoint to read sick leaves based on start date"""

    db_sickleave = crud.get_sickleaves_by_date(db, startDate=startDate)
    if db_sickleave is None:
        raise HTTPException(status_code=404, detail="Sick leave not found")
    return db_sickleave


@router.post("/create_sickleave", response_model=schemas.SickLeave)
async def create_sickleave(sickleave: schemas.SickLeaveCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a sick leave"""

    db_sickleave = db.query(models.SickLeave).filter(
            models.SickLeave.employeeNo == sickleave.employeeNo,
            models.SickLeave.startDate == sickleave.startDate).first()
    if db_sickleave:
        raise HTTPException(status_code=400,
                            detail="Sick leave already exists for employee")
    return crud.create_sickleave(db=db, sickleave=sickleave)


@router.put("/update_sickleave/{employeeNo}/{startDate}", 
        response_model=schemas.SickLeave)
async def update_sickleave(
        employeeNo: int, startDate: date, 
        sickleave_update: schemas.SickLeaveBase,
        db: Session = Depends(get_db)):
    """Endpoint to update a sick leave based on employeeNo and startDate"""

    return crud.update_sickleave(db, employeeNo, startDate, sickleave_update)


@router.delete("/delete_sickleave/{employeeNo}/{startDate}",
        response_model=schemas.SickLeave)
async def delete_sickleave(
        employeeNo: int, startDate: date,
        sickleave_delete: schemas.SickLeaveBase,
        db: Session = Depends(get_db)):
    """Endpoint to delete a sick leave based on employeeNo and startDate"""

    crud.delete_sickleave(db, employeeNo, startDate, sickleave_update)
    return {"message": "Sick leave deleted successfully"}
