# Import module
import sqlite3
from flask import Flask, jsonify, render_template, request, g


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

