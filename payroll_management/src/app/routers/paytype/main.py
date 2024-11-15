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


@router.get("/get_paytypes", response_model=List[schemas.PayType])
async def read_paytypes(skip: int = 0, limit: int = 100,
                         db: Session = Depends(get_db)):
    """Endpoint to read all pay types"""

    paytypes = crud.get_paytypes(db, skip=skip, limit=limit)
    return paytypes


@router.get("/get_paytype_by_no/{payTypeNo}",
            response_model=schemas.PayType)
async def read_paytype_no(payTypeNo: int, db: Session = Depends(get_db)):
    """Endpoint to read pay type based on its number"""

    db_paytype = crud.get_paytype_by_id(db, payTypeNo=payTypeNo)
    if db_paytype is None:
        raise HTTPException(status_code=404, detail="Pay type not found")
    return db_paytype


@router.get("/get_paytype_by_description", response_model=schemas.PayType)
async def read_paytype_description(payDescription: str,
        db: Session = Depends(get_db)):
    """Endpoint to read pay type based on its description"""

    db_paytype = crud.get_paytype_by_name(db, payDescription=payDescription)
    if db_paytype is None:
        raise HTTPException(status_code=404, detail="Pay type not found")
    return db_paytype


@router.post("/create_paytype", response_model=schemas.PayType)
async def create_paytype(paytype: schemas.PayTypeCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a pay type"""

    db_paytype = crud.get_paytype_by_name(
            db, payDescription=paytype.payDescription)
    if db_paytype:
        raise HTTPException(status_code=400,
                            detail="Pay type already exists")
    return crud.create_paytype(db=db, paytype=paytype)


@router.put("/update_paytype/{payTypeNo}", response_model=schemas.PayType)
async def update_paytype(payTypeNo: int,
        paytype_update: schemas.PayTypeBase,
        db: Session = Depends(get_db)):
    """Endpoint to update pay type based on its number"""

    return crud.update_paytype(db, payTypeNo, paytype_update)


@router.delete("/delete_paytype/{payTypeNo}", response_model=None)
async def delete_paytype(payTypeNo: int, db: Session = Depends(get_db)):
    """Endpoint to delete pay type based on its number"""

    crud.delete_paytype(db, payTypeNo)
    return {"message": "Pay type deleted successfully"}
