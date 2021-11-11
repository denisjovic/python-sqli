# Import module
import sqlite3
from flask import Flask, request


app = Flask(__name__)

@app.route('/test', methods=['POST'])
def query():
        if request.method == 'POST':
            passw = request.form['password']
            user = request.form['email']
            query = "SELECT * FROM employees WHERE username = '%s' AND password = '%s'" %(user,passw)

            return query
            