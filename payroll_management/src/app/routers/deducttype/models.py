#!/usr/bin/python3
"""Module that defines tables"""

from .database import Base
from sqlalchemy import Column, Integer, String


class DeductType(Base):
    """Class that defines deduct types"""

    __tablename__ = "deducttype"

    deductTypeNo = Column(Integer, primary_key=True, 
                        index=True, autoincrement=True)
    deductDescription = Column(String, unique=True, index=True)
