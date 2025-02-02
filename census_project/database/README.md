# Census Database Schema

This directory contains the SQL schema and database-related scripts for the **Census Database Management System**. It is designed to work with **PostgreSQL** and supports structured census data storage and retrieval.

## 📌 Database Overview
The database consists of multiple tables representing different aspects of the census, including:
- `households`: Stores household-related information.
- `individuals`: Contains demographic data of individuals.
- `housing_information`: Captures details of housing conditions.
- `agricultural_activity`: Records agricultural engagement details.
- `ict_and_disability`: Stores ICT access and disability-related information.

## 📂 Files in this Directory
- `schema.sql`: Contains the SQL commands to create tables, constraints, and relationships.
- `data.sql`: Sample data for testing purposes.
- `backup/`: Directory to store database backups.

## 🛠 Database Setup
### 1️⃣ Create PostgreSQL Database
Open PostgreSQL and run:
```sql
CREATE DATABASE census_db;
CREATE USER census_user WITH PASSWORD 'password';
ALTER ROLE census_user SET client_encoding TO 'utf8';
ALTER ROLE census_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE census_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE census_db TO census_user;
```

### 2️⃣ Load Schema
To create tables, run:
```bash
psql -U census_user -d census_db -f schema.sql
```

### 3️⃣ Insert Sample Data (Optional)
```bash
psql -U census_user -d census_db -f data.sql
```

## 🔄 Database Backup and Restore
### Backup Database
```bash
pg_dump -U census_user -d census_db -F c -f backup/census_db_backup.sql
```

### Restore Database
```bash
pg_restore -U census_user -d census_db backup/census_db_backup.sql
```

## 📡 Database Connection in Django
Ensure `census_project/settings.py` is configured with:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'census_db',
        'USER': 'census_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📜 License
This project is licensed under the MIT License.

---
### ✨ Need Help?
If you encounter issues, open a GitHub issue or contact the repository owner.
