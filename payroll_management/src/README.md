# Backend

## Content

* [About](#about)
* [Environment](#environment)
* [App](#app)
* [Db](#db)

## About

This directory contains the Payroll Management backend
infrastructure using [FastAPI](https://fastapi.tiangolo.com/)
and [PostgreSQL](https://www.postgresql.org/).

## Environment

Guide on setting up required environment to run
FastAPI app using `Python` version `3.10.12` ubuntu
`22.04`.

#### Setup
##### 1. Update System Packages
```
sudo apt update
sudo apt upgrade
```
##### 2. Install Pythin Package Management
```
sudo apt install python3-pip
```
##### 3. Create Virtual Environment
```
sudo apt install python3.8-venv
python3.8 -m venv myenv
source myenv/bin/activate
```
##### 4. Install Requirements
```
sudo pip install -r requirements.txt
```
##### 5. Install postgres
```
sudo apt install postgresql postgresql-contrib
```
##### 6. Start PostgreSQL Service
```
sudo service postgresql start
sudo systemctl enable postgresql
```
##### 7. Access PostgreSQL Prompt
```
psql
```
##### 8. Create Database and User
```
CREATE DATABASE your_database_name;
CREATE USER your_username WITH PASSWORD 'your_password';
ALTER ROLE your_username SET client_encoding TO 'utf8';
ALTER ROLE your_username SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_username SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;
ALTER USER your_username WITH SUPERUSER;
```
##### 9. Add `config.py` to [app](./app)
This file is not pushed to guthub because it contains
security details. This is an example of how it should look like:
```
#!/usr/bin/python3
"""Module that defines configuration settings"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Class that stores configuration items"""

    SECRET_KEY: str = "your_secret_key"
    ALGORITHM: str = "some_algorithm"
    MAIL_USERNAME: str = "smtp_mail_username"
    MAIL_PASSWORD: str = "smtp_mail_password"
    MAIL_FROM: str = "admin@clickinsureapi.com"
    MAIL_PORT: int = 25
    MAIL_SERVER: str = "sandbox.smtp.mailtrap.io"
    MAIL_STARTTLS: bool = False
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True
    ACCESS_TOKEN_DURATION_IN_MINUTES: float = 30.5
    REFRESH_TOKEN_DURATION_IN_MINUTES: float = 87000.5
    RESET_PASSWORD_SESSION_DURATION_IN_MINUTES: float = 1
    STATIC_DIR: str = ""
    API_BASE_URL: str = 'http://0.0.0.0:8000'
    COMPANY_URL: str = 'https://www.clickinsure.com'
    POSTGRES_USER: str = "your_username"
    POSTGRES_PASSWORD: str = "your_password"
    POSTGRES_DB: str = "yourdb"
    POSTGRES_DOMAIN: str = ("postgresql://user:your_password@localhost/your_db")

    class Config:
        title = 'Base Settings'
        env_file = '.env'


settings = Settings(
```
##### 10. Add `database.py` to [app](./app) and every router in [routers](./app/routers)
This file is also not pused to github because it conains db connection details
```
#!/usr/bin/python3
"""Module to define PostgreSQL database url"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL database URL
DATABASE_URL = "postgresql://user:your_password@localhost/your_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

## App

Run the application locally with:
```
uvicorn app.main:app --reload
```

## Db

This directory contains deyailed info on the Clickinsure database including:
* `Scripts` - to scrape raw data from wikipedia
* `dumps` - data dumps of current dataset
* `sql scripts` - sql scripts to create and manage tables for the database
* `ERD` - erd diagram of database

See [db](./db) for more details

