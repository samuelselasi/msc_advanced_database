#!/usr/bin/python3
"""Module to initialize routers and endpoints"""

from fastapi import FastAPI
from app import (employees, bonustype, deducttype, paytype,
        holiday, sickleave, payhistory, bonus, deduction)
import uvicorn

app = FastAPI(debug=True)

app.include_router(employees.router, tags=["Employees"])
app.include_router(bonustype.router, tags=["Bonus Types"])
app.include_router(deducttype.router, tags=["Deduct Types"])
app.include_router(paytype.router, tags=["Pay Types"])
app.include_router(holiday.router, tags=["Holidays"])
app.include_router(sickleave.router, tags=["Sick Leaves"])
app.include_router(payhistory.router, tags=["Pay History"])
app.include_router(bonus.router, tags=["Bonuses"])
app.include_router(deduction.router, tags=["Deductions"])

@app.get("/")
async def root():
    """Function that returns a default message when the root url is hit"""

    return {"message": "Payroll Management Database API. Hit /docs for swagger"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
