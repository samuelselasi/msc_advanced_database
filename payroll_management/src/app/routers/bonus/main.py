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


@router.get("/get_bonuses", response_model=List[schemas.Bonus])
async def read_bonuses(skip: int = 0, limit: int = 100,
                        db: Session = Depends(get_db)):
    """Endpoint to read all bonuses"""

    bonuses = crud.get_bonuses(db, skip=skip, limit=limit)
    return bonuses


@router.get("/get_bonuses_by_no/{employeeNo}",
        response_model=List[schemas.Bonus])
async def read_bonuses_no(employeeNo: int, db: Session = Depends(get_db)):
    """Endpoint to read bonus based on employee number"""

    db_bonus = crud.get_bonuses_by_id(db, employeeNo=employeeNo)
    if db_bonus is None:
        raise HTTPException(status_code=404, detail="Bonus not found")
    return db_bonus


@router.get("/get_bonus/{employeeNo}/{bonusDate}",
        response_model=schemas.Bonus)
async def get_bonus(
    employeeNo: int, bonusDate: date, db: Session = Depends(get_db)):
    """Endpoint to get a bonus based on employeeNo and bonusDate"""

    db_bonus = crud.get_bonus(db, employeeNo, bonusDate)
    if db_bonus is None:
        raise HTTPException(status_code=404, detail="Bonus not found")
    return db_bonus


@router.get("/get_bonus_by_date", response_model=List[schemas.Bonus])
async def read_bonus_date(bonusDate: str, db: Session = Depends(get_db)):
    """Endpoint to read bonus based on date"""

    db_bonus = crud.get_bonuses_by_date(db, bonusDate=bonusDate)
    if db_bonus is None:
        raise HTTPException(status_code=404, detail="Bonus not found")
    return db_bonus


@router.post("/create_bonus", response_model=schemas.Bonus)
async def create_bonus(bonus: schemas.BonusCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a bonus"""

    db_bonus = db.query(models.Bonus).filter(
            models.Bonus.employeeNo == bonus.employeeNo,
            models.Bonus.bonusDate == bonus.bonusDate).first()
    if db_bonus:
        raise HTTPException(status_code=400,
                            detail="Bonus already exists for employee")
    return crud.create_bonus(db=db, bonus=bonus)


@router.put("/update_bonus/{employeeNo}/{bonusDate}", 
        response_model=schemas.Bonus)
async def update_bonus(employeeNo: int, bonusDate: date,
        bonus_update: schemas.BonusBase, db: Session = Depends(get_db)):
    """Endpoint to update a bonus based on employeeNo and bonusDate"""

    return crud.update_bonus(db, employeeNo, bonusDate, bonus_update)


@router.delete("/delete_bonus/{employeeNo}/{bonusDate}",
        response_model=None)
async def delete_bonus(employeeNo: int, bonusDate: date,
        bonus_delete: schemas.BonusBase, db: Session = Depends(get_db)):
    """Endpoint to delete a bonus based on employeeNo and bonusDate"""

    crud.delete_bonus(db, employeeNo, bonusDate, bonus_delete)
    return {"message": "Bonus deleted successfully"}
