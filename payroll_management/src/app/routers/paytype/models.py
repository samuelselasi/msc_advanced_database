#!/usr/bin/python3
"""Module that defines tables"""

from .database import Base
from sqlalchemy import Column, Integer, String


class PayType(Base):
    """Class that defines pay types"""

    __tablename__ = "paytype"

    payTypeNo = Column(Integer, primary_key=True, 
                        index=True, autoincrement=True)
    payDescription = Column(String, unique=True, index=True)
