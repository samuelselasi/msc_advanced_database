#!/usr/bin/python3
"""Module that defines CRUD functions"""

from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_transaction_by_id(db: Session, transactionNo: int):
    """Function to return transactoion based on id"""

    return db.query(models.Transaction).filter(models.Transaction.transactionNo== transactionNo).first()


def get_transaction_by_name(db: Session, transactionDescription: str):
    """Function to return transaction based on name"""

    return db.query(models.Transaction).filter(
            models.Transaction.transactionDescription.ilike(f'%{transactionDescription}%')).first()


def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all transactions"""

    return db.query(models.Transaction).offset(skip).limit(limit).all()


def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    """Function to create a transaction"""

    db_transaction = models.Transaction(
            transactionDescription=transaction.transactionDescription,
            unitPrice=transaction.unitPrice,
            unitsOrdered=transaction.unitsOrdered,
            unitsReceived=transaction.unitsReceived,
            unitsSold=transaction.unitsSold,
            unitsWastage=transaction.unitsWastage,
            productNo=transaction.productNo,
            purchaseOrderNo=transaction.purchaseOrderNo)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def update_transaction(db: Session, transactionNo: int,
                    transaction_update: schemas.TransactionBase):
    """Function to update a transaction based on its id"""

    db_transaction = get_transaction_by_id(db, transactionNo=transactionNo)
    if db_transaction:
        for key, value in transaction_update.dict().items():
            setattr(db_transaction, key, value)
        db.commit()
        db.refresh(db_transaction)
        return db_transaction
    else:
        raise HTTPException(
                status_code=404, detail="Transaction not found")


def delete_transaction(db: Session, transactionNo: int):
    """Function to delete a transaction based on its id"""

    db_transaction = get_transaction_by_id(db, transactionNo=transactionNo)
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
    else:
        raise HTTPException(
                status_code=404, detail="Transaction not found")
