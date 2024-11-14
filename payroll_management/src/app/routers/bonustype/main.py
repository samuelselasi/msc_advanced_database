#!/usr/bin/python3
"""Module that defines endpoints functions"""

from typing import List
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


@router.get("/get_bonustypes", response_model=List[schemas.BonusType])
async def read_bonustypes(skip: int = 0, limit: int = 100,
                         db: Session = Depends(get_db)):
    """Endpoint to read all bonus types"""

    bonustypes = crud.get_bonustypes(db, skip=skip, limit=limit)
    return bonustypes


@router.get("/get_bonustype_by_no/{bonusTypeNo}",
            response_model=schemas.BonusType)
async def read_bonustype_no(bonusTypeNo: int, db: Session = Depends(get_db)):
    """Endpoint to read bonus type based on its number"""

    db_bonustype = crud.get_bonustype_by_id(db, bonusTypeNo=bonusTypeNo)
    if db_bonustype is None:
        raise HTTPException(status_code=404, detail="Bonus type not found")
    return db_bonustype


@router.get("/get_bonustype_by_description", response_model=schemas.BonusType)
async def read_bonustype_description(bonusDescription: str,
        db: Session = Depends(get_db)):
    """Endpoint to read bonus type based on its description"""

    db_bonustype = crud.get_bonustype_by_name(db, 
            bonusDescription=bonusDescription)
    if db_bonustype is None:
        raise HTTPException(status_code=404, detail="Bonus type not found")
    return db_bonustype


@router.post("/create_bonustype", response_model=schemas.BonusType)
async def create_bonustype(bonustype: schemas.BonusTypeCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a bonus type"""

    db_bonustype = crud.get_bonustype_by_name(
            db, bonusDescription=bonustype.bonusDescription)
    if db_bonustype:
        raise HTTPException(status_code=400,
                            detail="Bonus type already exists")
    return crud.create_bonustype(db=db, bonustype=bonustype)


@router.put("/update_bonustype/{bonusTypeNo}", response_model=schemas.BonusType)
async def update_bonustype(bonusTypeNo: int,
        bonustype_update: schemas.BonusTypeBase,
        db: Session = Depends(get_db)):
    """Endpoint to update bonus type based on its number"""

    return crud.update_bonustype(db, bonusTypeNo, bonustype_update)


@router.delete("/delete_bonustype/{bonusTypeNo}", response_model=None)
async def delete_bonustype(bonusTypeNo: int, db: Session = Depends(get_db)):
    """Endpoint to delete bonus type based on its number"""

    crud.delete_bonustype(db, bonusTypeNo)
    return {"message": "Bonus type deleted successfully"}
