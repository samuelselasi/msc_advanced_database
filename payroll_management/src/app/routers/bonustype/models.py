#!/usr/bin/python3
"""Module that defines tables"""

from .database import Base
from sqlalchemy import Column, Integer, String


class BonusType(Base):
    """Class that defines bonus types"""

    __tablename__ = "bonustype"

    bonusTypeNo = Column(Integer, primary_key=True, 
                        index=True, autoincrement=True)
    bonusDescription = Column(String, unique=True, index=True)
