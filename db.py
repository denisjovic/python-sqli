import sqlite3

def external_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    return cursor
