#!/usr/bin/python3
"""Module that defines authentication scheme"""

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
