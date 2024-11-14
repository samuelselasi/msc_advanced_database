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


@router.get("/get_suppliers", response_model=List[schemas.Supplier])
async def read_suppliers(skip: int = 0, limit: int = 100,
                         db: Session = Depends(get_db)):
    """Endpoint to read all suppliers"""

    suppliers = crud.get_suppliers(db, skip=skip, limit=limit)
    return suppliers


@router.get("/get_supplier_by_no/{supplierNo}",
            response_model=schemas.Supplier)
async def read_supplier_no(supplierNo: int, db: Session = Depends(get_db)):
    """Endpoint to read supplier based on its number"""

    db_supplier = crud.get_supplier_by_id(db, supplierNo=supplierNo)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier


@router.get("/get_supplier_by_name",
        response_model=schemas.Supplier)
async def read_supplier_name(supplierName: str,
        db: Session = Depends(get_db)):
    """Endpoint to read supplier based on its name"""

    db_supplier = crud.get_supplier_by_name(db, 
            supplierName=supplierName)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier


@router.get("/get_supplier_by_tel",
        response_model=schemas.Supplier)
async def read_supplier_tel(suppTelNo: str,
        db: Session = Depends(get_db)):
    """Endpoint to read supplier based on its telephone number"""

    db_supplier = crud.get_supplier_by_tel(db,
            suppTelNo=suppTelNo)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier


@router.get("/get_supplier_by_fax",
        response_model=schemas.Supplier)
async def read_supplier_fax(suppFaxNo: str,
        db: Session = Depends(get_db)):
    """Endpoint to read supplier based on its fax number"""

    db_supplier = crud.get_supplier_by_fax(db,
            suppFaxNo=suppFaxNo)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier


@router.post("/create_supplier", response_model=schemas.Supplier)
async def create_supplier(supplier: schemas.SupplierCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create a supplier"""

    db_supplier = crud.get_supplier_by_name(
            db, supplierName=supplier.supplierName)
    if db_supplier:
        raise HTTPException(status_code=400,
                            detail="Supplier already exists")
    return crud.create_supplier(db=db, supplier=supplier)


@router.put("/update_supplier/{supplierNo}", response_model=schemas.Supplier)
async def update_supplier(supplierNo: int,
        supplier_update: schemas.SupplierBase,
        db: Session = Depends(get_db)):
    """Endpoint to update supplier based on its number"""

    return crud.update_supplier(db, supplierNo, supplier_update)


@router.delete("/delete_supplier/{supplierNo}", response_model=None)
async def delete_supplier(supplierNo: int, db: Session = Depends(get_db)):
    """Endpoint to delete supplier based on its number"""

    crud.delete_supplier(db, supplierNo)
    return {"message": "Supplier deleted successfully"}
