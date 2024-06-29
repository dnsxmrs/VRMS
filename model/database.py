import sqlite3
import os
from config.database_config import DATABASE_PATH, DATABASE_FOLDER

def get_db_connection():
    if not os.path.exists(DATABASE_FOLDER):
        os.makedirs(DATABASE_FOLDER)
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def migrate_schema(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS vehicles (
                        id INTEGER PRIMARY KEY,
                        make TEXT,
                        model TEXT,
                        year INTEGER,
                        availability TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT,
                        email TEXT,
                        contact_info TEXT)''')

def ensure_schema():
    conn = get_db_connection()
    cursor = conn.cursor()
    migrate_schema(cursor)
    conn.commit()
    conn.close()
