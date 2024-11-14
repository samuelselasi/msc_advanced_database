#!/usr/bin/python3
"""Module that defines tables"""

from .database import Base
from sqlalchemy import Column, Integer, String


class ProductCategory(Base):
    """Class that defines types of product categories"""

    __tablename__ = "category"

    categoryNo = Column(Integer, primary_key=True, 
                        index=True, autoincrement=True)
    categoryDescription = Column(String, unique=True, index=True)
