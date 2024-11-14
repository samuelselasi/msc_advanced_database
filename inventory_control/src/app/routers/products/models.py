#!/usr/bin/python3
"""Module that defines tables"""

from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class ProductCategory(Base):
    """Class that defines types of product categories"""

    __tablename__ = "category"

    categoryNo = Column(Integer, primary_key=True, 
                        index=True, autoincrement=True)
    categoryDescription = Column(String, unique=True, index=True)

    product = relationship("Product", back_populates="category")


class Product(Base):
    """Class that defines types of product categories"""

    __tablename__ = "products"

    productNo = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)
    productName = Column(String, unique=True, index=True)
    serialNo = Column(String, unique=True, index=True)
    unitPrice = Column(Integer, nullable=False)
    quantityOnHand = Column(Integer, nullable=False)
    reorderLevel = Column(Integer, nullable=False)
    reorderQuantity = Column(Integer, nullable=False)
    reorderLeadTime = Column(Integer, nullable=False)
    categoryNo = Column(Integer, ForeignKey("category.categoryNo"))

    category = relationship("ProductCategory", back_populates="product")
