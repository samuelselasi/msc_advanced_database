#!/usr/bin/python3
"""Module that defines CRUD functions"""

from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_product_by_id(db: Session, productNo: int):
    """Function to return product based on id"""

    return db.query(models.Product).filter(models.Product.productNo == productNo).first()


def get_product_by_name(db: Session, productName: str):
    """Function to return product based on name"""

    return db.query(models.Product).filter(
            models.Product.productName.ilike(f'%{productName}%')).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all products"""

    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    """Function to create a product"""

    db_product = models.Product(
            productName=product.productName,
            serialNo=product.serialNo,
            unitPrice=product.unitPrice,
            quantityOnHand=product.quantityOnHand,
            reorderLevel=product.reorderLevel,
            reorderQuantity=product.reorderQuantity,
            reorderLeadTime=product.reorderLeadTime,
            categoryNo=product.categoryNo)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, productNo: int,
                    product_update: schemas.ProductBase):
    """Function to update a product based on its id"""

    db_product = get_product_by_id(db, productNo=productNo)
    if db_product:
        for key, value in product_update.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return db_product
    else:
        raise HTTPException(status_code=404, detail="Product not found")


def delete_product(db: Session, productNo: int):
    """Function to delete a product based on its id"""

    db_product = get_product_by_id(db, productNo=productNo)
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Product not found")
