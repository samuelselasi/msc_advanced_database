#!/bin/bash

# Check if the script is run as root or with sudo
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root or with sudo."
    exit 1
fi

# Read user input for the username, password, and database name
read -p "Enter PostgreSQL username: " username
read -s -p "Enter PostgreSQL password: " password
echo
read -p "Enter PostgreSQL database name: " dbname

# Install PostgreSQL if not already installed
if ! command -v psql &> /dev/null; then
    apt update
    apt install -y postgresql
fi

# Start PostgreSQL service
systemctl start postgresql

# Create user and database
sudo -u postgres psql -c "CREATE USER $username WITH PASSWORD '$password';"
sudo -u postgres psql -c "CREATE DATABASE $dbname;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $dbname TO $username;"

# Enable PostgreSQL to start at boot
systemctl enable postgresql

# Display success message
echo "PostgreSQL user '$username' and database '$dbname' created successfully."

# Exit
exit 0
