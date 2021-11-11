import db

from flask import Flask, request

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = db.external_db()
        
        # cur.execute("SELECT * FROM employees WHERE username = '%s' AND password = '%s'" %(username,password))
        cur.execute(f"SELECT * FROM employees WHERE username = ${username} AND password = ${password}")
        cur.commit()
        cur.close()

