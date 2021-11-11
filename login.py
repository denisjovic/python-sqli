# Import module
import sqlite3
from flask import Flask, request


app = Flask(__name__)


# Connecting to sqlite
def connectToDB():
    conn = sqlite3.connect('gfg.db')
    cursor = conn.cursor()
    return cursor


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['email']
        passw = request.form['password']

        cur = connectToDB()
        
        cur.execute("SELECT * FROM employees WHERE username = '%s' AND password = '%s'" %(user,passw))
        cur.commit()
        cur.close()

