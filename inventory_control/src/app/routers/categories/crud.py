#!/usr/bin/python3
"""Module that defines CRUD functions"""

from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_category_by_id(db: Session, categoryNo: int):
    """Function to return category based on id"""

    return db.query(models.ProductCategory).filter(models.ProductCategory.categoryNo == categoryNo).first()


def get_category_by_name(db: Session, categoryDescription: str):
    """Function to return category based on name"""

    return db.query(models.ProductCategory).filter(
            models.ProductCategory.categoryDescription.ilike(f'%{categoryDescription}%')).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all categories"""

    return db.query(models.ProductCategory).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    """Function to create a category"""

    db_category = models.ProductCategory(categoryDescription=category.categoryDescription)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, categoryNo: int,
                    category_update: schemas.CategoryBase):
    """Function to update a category based on its id"""

    db_category = get_category_by_id(db, categoryNo=categoryNo)
    if db_category:
        for key, value in category_update.dict().items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
        return db_category
    else:
        raise HTTPException(status_code=404, detail="Category not found")


def delete_category(db: Session, categoryNo: int):
    """Function to delete a category based on its id"""

    db_category = get_category_by_id(db, categoryNo=categoryNo)
    if db_category:
        db.delete(db_category)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Category not found")
