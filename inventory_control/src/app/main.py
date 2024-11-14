#!/usr/bin/python3
"""Module to initialize routers and endpoints"""

from fastapi import FastAPI
from app.routers.categories import main as categories
from app.routers.products import main as products
from app.routers.suppliers import main as suppliers
from app.routers.employees import main as employees
from app.routers.orders import main as orders
from app.routers.transactions import main as transactions

app = FastAPI(debug=True)

app.include_router(categories.router, tags=["Product Categories"])
app.include_router(products.router, tags=["Products"])
app.include_router(suppliers.router, tags=["Suppliers"])
app.include_router(employees.router, tags=["Employees"])
app.include_router(orders.router, tags=["Purchase Orders"])
app.include_router(transactions.router, tags=["Transactions"])


@app.get("/")
async def root():
    """Function that returns a default message when the root url is hit"""

    return {"message": "Inventory Control Database API. Hit /docs for swagger"}
