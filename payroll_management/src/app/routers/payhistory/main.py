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


@router.get("/get_payhistories", response_model=List[schemas.PayHistory])
async def read_payhistories(skip: int = 0, limit: int = 100,
                        db: Session = Depends(get_db)):
    """Endpoint to read all pay histories"""

    payhistory = crud.get_payhistories(db, skip=skip, limit=limit)
    return payhistory


@router.get("/get_payhistory_by_no/{payNo}",
        response_model=schemas.PayHistory)
async def read_payhistory_no(payNo: int, db: Session = Depends(get_db)):
    """Endpoint to read pay history based on its number"""

    db_payhistory = crud.get_payhistory_by_id(db, payNo=payNo)
    if db_payhistory is None:
        raise HTTPException(status_code=404, detail="Pay history not found")
    return db_payhistory


@router.get("/get_payhistories_emp/{employeeNo}/",
        response_model=List[schemas.PayHistory])
async def get_payhistories_emp(
        employeeNo: int, db: Session = Depends(get_db)):
    """Endpoint to get pay histories based on employeeNo"""

    db_payhistory = crud.get_payhistory_by_emp(db, employeeNo)
    if db_payhistory is None:
        raise HTTPException(status_code=404, detail="Pay history not found")
    return db_payhistory


@router.post("/create_payhistory", response_model=schemas.PayHistory)
async def create_payhistory(payhistory: schemas.PayHistoryCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a pay history"""

    db_payhistory = db.query(models.PayHistory).filter(
            models.PayHistory.employeeNo == payhistory.employeeNo,
            models.PayHistory.payDate == payhistory.payDate).first()
    if db_payhistory:
        raise HTTPException(status_code=400,
                            detail="Payhistory already exists")
    return crud.create_payhistory(db=db, payhistory=payhistory)


@router.put("/update_payhistory/{payNo}", 
        response_model=schemas.PayHistory)
async def update_payhistory(
        payNo: int, payhistory_update: schemas.PayHistoryBase,
        db: Session = Depends(get_db)):
    """Endpoint to update a pay history based on id"""

    return crud.update_payhistory(db, payNo, payhistory_update)


@router.delete("/delete_payhistory/{payNo}",
        response_model=schemas.PayHistory)
async def delete_payhistory(
        payNo: int, payhistory_delete: schemas.PayHistoryBase,
        db: Session = Depends(get_db)):
    """Endpoint to delete a pay history based on id"""

    crud.delete_payhistory(db, payNo, payhistory_delete)
    return {"message": "Pay history deleted successfully"}
