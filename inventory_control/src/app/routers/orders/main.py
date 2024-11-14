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


@router.get("/get_orders", response_model=List[schemas.Order])
async def read_orders(skip: int = 0, limit: int = 100,
                         db: Session = Depends(get_db)):
    """Endpoint to read all purchase orders"""

    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders


@router.get("/get_order_by_no/{purchaseOrderNo}", response_model=schemas.Order)
async def read_order_no(purchaseOrderNo: int, db: Session = Depends(get_db)):
    """Endpoint to read purchase order based on its number"""

    db_order = crud.get_order_by_id(db, purchaseOrderNo=purchaseOrderNo)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Purchase order not found")
    return db_order


@router.get("/get_order_by_name", response_model=schemas.Order)
async def read_order_name(
        purchaseOrderDescription: str, db: Session = Depends(get_db)):
    """Endpoint to read purchase order based on its name"""

    db_order = crud.get_order_by_name(
            db, purchaseOrderDescription=purchaseOrderDescription)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Purchase order not found")
    return db_order


@router.post("/create_order", response_model=schemas.Order)
async def create_order(order: schemas.OrderCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a purchase order"""

    db_order = crud.get_order_by_name(
            db, purchaseOrderDescription=order.purchaseOrderDescription)
    if db_order:
        raise HTTPException(status_code=400,
                            detail="Purchase order already exists")
    return crud.create_order(db=db, order=order)


@router.put("/update_order/{purchaseOrderNo}", response_model=schemas.Order)
async def update_order(
        purchaseOrderNo: int, order_update: schemas.OrderBase,
        db: Session = Depends(get_db)):
    """Endpoint to update purchase order based on its number"""

    return crud.update_order(db, purchaseOrderNo, order_update)


@router.delete("/delete_order/{purchaseOrderNo}", response_model=None)
async def delete_order(purchaseOrderNo: int, db: Session = Depends(get_db)):
    """Endpoint to delete purchase order based on its number"""

    crud.delete_order(db, purchaseOrderNo)
    return {"message": "Purchase order deleted successfully"}
