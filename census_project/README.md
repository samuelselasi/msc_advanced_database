# Census Database Management System

This is a Django-based Population and Census Database Management System designed for Ghana. It utilizes **PostgreSQL** as the database backend and provides a RESTful API using Django REST Framework.

## 📌 Project Repository
GitHub: [Census Project](https://github.com/samuelselasi/msc_advanced_database/tree/main/census_project)

## ⚡ Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- PostgreSQL (>= 12)
- Git
- Virtual Environment (venv or virtualenv)

## 🔽 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/samuelselasi/msc_advanced_database.git
cd msc_advanced_database/census_project
```

### 2️⃣ Create a Virtual Environment and Activate It
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🛠 Database Setup
### 4️⃣ Create PostgreSQL Database
Open PostgreSQL and run:
```sql
CREATE DATABASE census_db;
CREATE USER census_user WITH PASSWORD 'password';
ALTER ROLE census_user SET client_encoding TO 'utf8';
ALTER ROLE census_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE census_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE census_db TO census_user;
```

### 5️⃣ Configure Django Database Settings
Edit `census_project/settings.py` and update:
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

## 🚀 Running the Project
### 6️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7️⃣ Create a Superuser (Optional for Admin Access)
```bash
python manage.py createsuperuser
```

### 8️⃣ Start the Development Server
```bash
python manage.py runserver
```
Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📡 API Endpoints
You can explore the API at:
- Swagger UI: `http://127.0.0.1:8000/docs/`
- Django Admin: `http://127.0.0.1:8000/admin/`

## 🔄 Backup Database
To create a backup:
```bash
python manage.py dumpdata > backup.json
```
To restore:
```bash
python manage.py loaddata backup.json
```

## 📝 License
This project is licensed under the MIT License.

---
### ✨ Need Help?
If you run into any issues, please open an issue on GitHub or contact the repository owner.
