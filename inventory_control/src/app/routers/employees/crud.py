#!/usr/bin/python3
"""Module that defines CRUD functions"""

from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_employee_by_id(db: Session, employeeNo: int):
    """Function to return employee based on id"""

    return db.query(models.Employee).filter(models.Employee.employeeNo == employeeNo).first()


def get_employee_by_name(db: Session, employeeName: str):
    """Function to return employee based on name"""

    return db.query(models.Employee).filter(
            models.Employee.employeeName.ilike(f'%{employeeName}%')).first()


def get_employee_by_tel(db: Session, employeeTelNo: str):
    """Function to return employee based on telephone number"""

    return db.query(models.Employee).filter(
            models.Employee.employeeTelNo.ilike(f'%{employeeTelNo}%')).first()

def get_employee_by_fax(db: Session, employeeFaxNo: str):
    """Function to return employee based on fax number"""

    return db.query(models.Employee).filter(
            models.Employee.employeeFaxNo.ilike(f'%{employeeFaxNo}%')).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    """Function to return all employees"""

    return db.query(models.Employee).offset(skip).limit(limit).all()


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    """Function to create an employee"""

    db_employee = models.Employee(
            employeeName=employee.employeeName,
            employeeCity=employee.employeeCity,
            employeeState=employee.employeeState,
            employeeZipCode=employee.employeeZipCode,
            employeeTelNo=employee.employeeTelNo,
            employeeFaxNo=employee.employeeFaxNo,
            employeeEmailAddress=employee.employeeEmailAddress)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db: Session, employeeNo: int,
                    employee_update: schemas.EmployeeBase):
    """Function to update an employee based on its id"""

    db_employee = get_employee_by_id(db, employeeNo=employeeNo)
    if db_employee:
        for key, value in employee_update.dict().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    else:
        raise HTTPException(status_code=404, detail="Employee not found")


def delete_employee(db: Session, employeeNo: int):
    """Function to delete an employee based on its id"""

    db_employee = get_employee_by_id(db, employeeNo=employeeNo)
    if db_employee:
        db.delete(db_employee)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Employee not found")
