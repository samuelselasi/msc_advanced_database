#!/bin/bash

# Variables
HOST="localhost"
PORT="5432"
USERNAME="admin"
DATABASE="census"
BACKUP_DIR="./backups/"
DATE=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR${DATABASE}_backup_$DATE.sql"

# Ensure the backup directory exists
mkdir -p "$BACKUP_DIR"

# Perform the backup using pg_dump
pg_dump -h "$HOST" -p "$PORT" -U "$USERNAME" -F p -b -v -f "$BACKUP_FILE" "$DATABASE"

# pg_dump -h "$HOST" -p "$PORT" -U "$USERNAME" -F c -b -v -f "$BACKUP_FILE" "$DATABASE"

# Check if the backup was successful
if [ $? -eq 0 ]; then
    echo "Backup successful! File saved at: $BACKUP_FILE"
else
    echo "Backup failed!"
    exit 1
fi
