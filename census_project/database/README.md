# Census Project Database Setup

This directory contains the SQL scripts necessary for setting up the database schema for the Census Project. Follow the instructions below to create and populate the database.

## Prerequisites

- **PostgreSQL**: Ensure that PostgreSQL is installed on your system. You can download it from the [official website](https://www.postgresql.org/download/).

## Setup Instructions

1. **Create the Database**:
   - Open your terminal or command prompt.
   - Access the PostgreSQL command-line interface:
     ```bash
     psql -U your_username
     ```
   - Create a new database named `census_db`:
     ```sql
     CREATE DATABASE census_db;
     ```

2. **Navigate to the Database Directory**:
   - In your terminal, navigate to the `database` directory of the project:
     ```bash
     cd path/to/census_project/database
     ```

3. **Execute SQL Scripts**:
   - The SQL scripts are organized to set up different parts of the database schema. Execute each script in the appropriate order to ensure all dependencies are met. For example:
     ```bash
     psql -U your_username -d census_db -f create_tables.sql
     psql -U your_username -d census_db -f insert_data.sql
     psql -U your_username -d census_db -f create_indexes.sql
     ```
   - Replace `your_username` with your PostgreSQL username.
   - Ensure you execute the scripts in the correct order to maintain referential integrity.

4. **Verify the Setup**:
   - After executing the scripts, you can verify the tables and data by connecting to the `census_db` database:
     ```bash
     psql -U your_username -d census_db
     ```
   - List the tables:
     ```sql
     \dt
     ```
   - View sample data:
     ```sql
     SELECT * FROM household LIMIT 10;
     ```

## Notes

- If you encounter any issues during the setup, ensure that your PostgreSQL service is running and that you have the necessary permissions to create databases and execute scripts.
- It's recommended to review each SQL script to understand its purpose and ensure it aligns with your database design.

For more detailed information about the project and its components, refer to the main [README](../README.md) file in the root directory.

### ✨ Need Help?
If you encounter issues, open a GitHub issue or contact the repository owner.
