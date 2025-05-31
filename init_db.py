#!/usr/bin/env python3
import sqlite3

def setup_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Clear previous data
    cursor.execute("DELETE FROM users")

    # Insert sample data
    sample_users = [('Alice',), ('Bob',), ('Charlie',)]
    cursor.executemany("INSERT INTO users (name) VALUES (?)", sample_users)

    conn.commit()
    conn.close()
    print("✅ users.db has been set up with sample users.")

if __name__ == "__main__":
    setup_database()

