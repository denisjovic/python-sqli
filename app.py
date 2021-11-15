# Import module
import sqlite3
from flask import Flask, request


app = Flask(__name__)


  
# Connecting to sqlite
conn = sqlite3.connect('gfg.db')
cursor = conn.cursor()


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['email']
        passw = request.form['password']
        
        cursor.execute("SELECT * FROM employees WHERE username = '%s' AND password = '%s'" %(user,passw))
        conn.commit()
        conn.close()

@app.route('/update', methods=['PUT'])
def update():
        if request.method == 'PUT':
            passw = request.form['password']
            user = request.form['email']

            cursor.execute("UPDATE users SET password = '%s' WHERE user = '%s' " % (user, passw))
            conn.commit()
            conn.close()




