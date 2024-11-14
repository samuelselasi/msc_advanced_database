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


@router.get("/get_categories", response_model=List[schemas.ProductCategory])
async def read_categories(skip: int = 0, limit: int = 100,
                         db: Session = Depends(get_db)):
    """Endpoint to read all categories"""

    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories


@router.get("/get_category_by_no/{categoryNo}",
            response_model=schemas.ProductCategory)
async def read_category_no(categoryNo: int, db: Session = Depends(get_db)):
    """Endpoint to read category based on its number"""

    db_category = crud.get_category_by_id(db, categoryNo=categoryNo)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.get("/get_category_by_description",
        response_model=schemas.ProductCategory)
async def read_category_description(categoryDescription: str,
        db: Session = Depends(get_db)):
    """Endpoint to read category based on its description"""

    db_category = crud.get_category_by_name(db, 
            categoryDescription=categoryDescription)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.post("/create_category", response_model=schemas.ProductCategory)
async def create_category(category: schemas.CategoryCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a category"""

    db_category = crud.get_category_by_name(
            db, categoryDescription=category.categoryDescription)
    if db_category:
        raise HTTPException(status_code=400,
                            detail="Category already exists")
    return crud.create_category(db=db, category=category)


@router.put("/update_category/{categoryNo}", response_model=schemas.ProductCategory)
async def update_category(categoryNo: int,
        category_update: schemas.CategoryBase,
        db: Session = Depends(get_db)):
    """Endpoint to update category based on its number"""

    return crud.update_category(db, categoryNo, category_update)


@router.delete("/delete_category/{categoryNo}", response_model=None)
async def delete_category(categoryNo: int, db: Session = Depends(get_db)):
    """Endpoint to delete category based on its number"""

    crud.delete_category(db, categoryNo)
    return {"message": "Category deleted successfully"}
