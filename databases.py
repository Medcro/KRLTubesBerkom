import sqlite3


def create_table_if_not_exists():
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def add_user(first_name, last_name, age):
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES (?, ?, ?)",
                   (first_name, last_name, age))
    conn.commit()
    conn.close()


def get_all_users():
    conn = sqlite3.connect('data_diri.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users
