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


@router.get("/get_products", response_model=List[schemas.Product])
async def read_products(skip: int = 0, limit: int = 100,
                         db: Session = Depends(get_db)):
    """Endpoint to read all products"""

    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@router.get("/get_product_by_no/{productNo}", response_model=schemas.Product)
async def read_product_no(productNo: int, db: Session = Depends(get_db)):
    """Endpoint to read product based on its number"""

    db_product = crud.get_product_by_id(db, productNo=productNo)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.get("/get_product_by_name", response_model=schemas.Product)
async def read_product_name(productName: str, db: Session = Depends(get_db)):
    """Endpoint to read product based on its name"""

    db_product = crud.get_product_by_name(db, productName=productName)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.post("/create_product", response_model=schemas.Product)
async def create_product(product: schemas.ProductCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a product"""

    db_product = crud.get_product_by_name(db, productName=product.productName)
    if db_product:
        raise HTTPException(status_code=400,
                            detail="Product already exists")
    return crud.create_product(db=db, product=product)


@router.put("/update_product/{productNo}", response_model=schemas.Product)
async def update_product(
        productNo: int, product_update: schemas.ProductBase,
        db: Session = Depends(get_db)):
    """Endpoint to update product based on its number"""

    return crud.update_product(db, productNo, product_update)


@router.delete("/delete_product/{productNo}", response_model=None)
async def delete_product(productNo: int, db: Session = Depends(get_db)):
    """Endpoint to delete product based on its number"""

    crud.delete_product(db, productNo)
    return {"message": "Product deleted successfully"}
