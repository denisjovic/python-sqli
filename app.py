# Import module
import sqlite3
from flask import Flask, jsonify, render_template, request, g

app = Flask(__name__)

# Connecting to sqlite
def connectToDB():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    return cursor


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['email']
        passw = request.form['password']
        
        connectToDB.execute("SELECT * FROM employees WHERE username = '%s' AND password = '%s'" %(user,passw))
        connectToDB.commit()
        connectToDB.close()

