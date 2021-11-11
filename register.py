import db

from flask import Flask, request

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db.external_db.execute("SELECT * FROM employees WHERE username = '%s' AND password = '%s'" %(username,password))
        db.external_db.commit()
        db.external_db.close()

