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


@router.get("/get_transactions", response_model=List[schemas.Transaction])
async def read_transactions(skip: int = 0, limit: int = 100,
                         db: Session = Depends(get_db)):
    """Endpoint to read all transactions"""

    transactions = crud.get_transactions(db, skip=skip, limit=limit)
    return transactions


@router.get("/get_transaction_by_no/{transactionNo}",
        response_model=schemas.Transaction)
async def read_transaction_no(transactionNo: int, db: Session = Depends(get_db)):
    """Endpoint to read transaction based on its number"""

    db_transaction = crud.get_transaction_by_id(db, transactionNo=transactionNo)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction


@router.get("/get_transaction_by_name", response_model=schemas.Transaction)
async def read_transaction_name(
        transactionDescription: str, db: Session = Depends(get_db)):
    """Endpoint to read transaction based on its name"""

    db_transaction = crud.get_transaction_by_name(
            db, transactionDescription=transactionDescription)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Trasaction not found")
    return db_transaction


@router.post("/create_transaction", response_model=schemas.Transaction)
async def create_transaction(transaction: schemas.TransactionCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a transaction"""

    db_transaction = crud.get_transaction_by_name(
            db, transactionDescription=transaction.transactionDescription)
    if db_transaction:
        raise HTTPException(status_code=400,
                            detail="Transaction already exists")
    return crud.create_transaction(db=db, transaction=transaction)


@router.put("/update_transaction/{transactionNo}", response_model=schemas.Transaction)
async def update_transaction(
        transactionNo: int, transaction_update: schemas.TransactionBase,
        db: Session = Depends(get_db)):
    """Endpoint to update transaction based on its number"""

    return crud.update_transaction(db, transactionNo, transaction_update)


@router.delete("/delete_transaction/{transactionNo}", response_model=None)
async def delete_transaction(transactionNo: int, db: Session = Depends(get_db)):
    """Endpoint to delete transaction based on its number"""

    crud.delete_transaction(db, transactionNo)
    return {"message": "Transaction deleted successfully"}
