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


@router.get("/get_employees", response_model=List[schemas.Employee])
async def read_employees(skip: int = 0, limit: int = 100,
                         db: Session = Depends(get_db)):
    """Endpoint to read all employees"""

    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees


@router.get("/get_employee_by_no/{employeeNo}",
            response_model=schemas.Employee)
async def read_employee_no(employeeNo: int, db: Session = Depends(get_db)):
    """Endpoint to read employee based on its number"""

    db_employee = crud.get_employee_by_id(db, employeeNo=employeeNo)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@router.get("/get_employee_by_name",
        response_model=schemas.Employee)
async def read_employee_name(employeeName: str,
        db: Session = Depends(get_db)):
    """Endpoint to read employee based on its name"""

    db_employee = crud.get_employee_by_name(db, 
            employeeName=employeeName)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@router.get("/get_employee_by_tel",
        response_model=schemas.Employee)
async def read_employee_tel(employeeTelNo: str,
        db: Session = Depends(get_db)):
    """Endpoint to read employee based on its telephone number"""

    db_employee = crud.get_employee_by_tel(db,
            employeeTelNo=employeeTelNo)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@router.get("/get_employee_by_fax",
        response_model=schemas.Employee)
async def read_employee_fax(employeeFaxNo: str,
        db: Session = Depends(get_db)):
    """Endpoint to read employee based on its fax number"""

    db_employee = crud.get_employee_by_fax(db,
            employeeFaxNo=employeeFaxNo)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@router.post("/create_employee", response_model=schemas.Employee)
async def create_employee(employee: schemas.EmployeeCreate,
        db: Session = Depends(get_db)):
    """Endpoint to create an employee"""

    db_employee = crud.get_employee_by_name(
            db, employeeName=employee.employeeName)
    if db_employee:
        raise HTTPException(status_code=400,
                            detail="Employee already exists")
    return crud.create_employee(db=db, employee=employee)


@router.put("/update_employee/{employeeNo}", response_model=schemas.Employee)
async def update_employee(employeeNo: int,
        employee_update: schemas.EmployeeBase,
        db: Session = Depends(get_db)):
    """Endpoint to update employee based on its number"""

    return crud.update_employee(db, employeeNo, employee_update)


@router.delete("/delete_employee/{employeeNo}", response_model=None)
async def delete_employee(employeeNo: int, db: Session = Depends(get_db)):
    """Endpoint to delete employee based on its number"""

    crud.delete_employee(db, employeeNo)
    return {"message": "Employee deleted successfully"}
