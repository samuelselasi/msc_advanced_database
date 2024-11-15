#!/usr/bin/python3
"""Module to initialize routers and endpoints"""

from fastapi import FastAPI
from app.routers.employees import main as employees
from app.routers.bonustype import main as bonustype
from app.routers.deducttype import main as deducttype
from app.routers.paytype import main as paytype
from app.routers.holiday import main as holiday

app = FastAPI(debug=True)

app.include_router(employees.router, tags=["Employees"])
app.include_router(bonustype.router, tags=["Bonus Types"])
app.include_router(deducttype.router, tags=["Deduct Types"])
app.include_router(paytype.router, tags=["Pay Types"])
app.include_router(holiday.router, tags=["Holidays"])

@app.get("/")
async def root():
    """Function that returns a default message when the root url is hit"""

    return {"message": "Payroll Management Database API. Hit /docs for swagger"}
