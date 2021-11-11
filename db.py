import sqlite3

def external_db():
    conn = sqlite3.connect('gfg.db')
    cursor = conn.cursor()

def test():
    print('Test func')