#!/usr/bin/python3
"""Module that defines utilities"""

import jwt
import random
import string
from typing import Optional
from app.config import settings
from datetime import datetime, timedelta

uppercase_and_digits = string.ascii_uppercase + string.digits
lowercase_and_digits = string.ascii_lowercase + string.digits


def gen_alphanumeric_code(length):
    """Function to generate alpha-numeric code"""

    code = ''.join((random.choice(uppercase_and_digits)
                   for i in range(length)))
    return code


def create_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Function to create access token for current user"""

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_token(*, data: str):
    """Function to decode access token"""

    to_decode = data
    return jwt.decode(to_decode,
                      settings.SECRET_KEY,
                      algorithms=settings.ALGORITHM)
