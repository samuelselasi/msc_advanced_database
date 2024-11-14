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


@router.get("/get_deducttypes", response_model=List[schemas.DeductType])
async def read_deducttypes(skip: int = 0, limit: int = 100,
                         db: Session = Depends(get_db)):
    """Endpoint to read all deduct types"""

    deducttypes = crud.get_deducttypes(db, skip=skip, limit=limit)
    return deducttypes


@router.get("/get_deducttype_by_no/{deductTypeNo}",
            response_model=schemas.DeductType)
async def read_deducttype_no(deductTypeNo: int, db: Session = Depends(get_db)):
    """Endpoint to read deduct type based on its number"""

    db_deducttype = crud.get_deducttype_by_id(db, deductTypeNo=deductTypeNo)
    if db_deducttype is None:
        raise HTTPException(status_code=404, detail="Deduct type not found")
    return db_deducttype


@router.get("/get_deducttype_by_description", response_model=schemas.DeductType)
async def read_deducttype_description(deductDescription: str,
        db: Session = Depends(get_db)):
    """Endpoint to read deduct type based on its description"""

    db_deducttype = crud.get_deducttype_by_name(db, 
            deductDescription=deductDescription)
    if db_deducttype is None:
        raise HTTPException(status_code=404, detail="Deduct type not found")
    return db_deducttype


@router.post("/create_deducttype", response_model=schemas.DeductType)
async def create_deducttype(deducttype: schemas.DeductTypeCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a deduct type"""

    db_deducttype = crud.get_deducttype_by_name(
            db, deductDescription=deducttype.deductDescription)
    if db_deducttype:
        raise HTTPException(status_code=400,
                            detail="Deduct type already exists")
    return crud.create_deducttype(db=db, deducttype=deducttype)


@router.put("/update_deducttype/{deductTypeNo}", response_model=schemas.DeductType)
async def update_deducttype(deductTypeNo: int,
        deducttype_update: schemas.DeductTypeBase,
        db: Session = Depends(get_db)):
    """Endpoint to update deduct type based on its number"""

    return crud.update_deducttype(db, deductTypeNo, deducttype_update)


@router.delete("/delete_deducttype/{deductTypeNo}", response_model=None)
async def delete_deducttype(deductTypeNo: int, db: Session = Depends(get_db)):
    """Endpoint to delete deduct type based on its number"""

    crud.delete_deducttype(db, deductTypeNo)
    return {"message": "Deduct type deleted successfully"}
