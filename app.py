import sqlite3, os, hashlib
from flask import Flask, jsonify, render_template, request, g

app = Flask(__name__)
app.database = "sample.db"

def connect_db():
    return sqlite3.connect(app.database)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.json['username']
        passw = request.json['password']
        g.db = connect_db()
        cur = g.db.execute("SELECT * FROM employees WHERE username = '%s' AND password = '%s'" %(user,passw))
        if cur.fetchone():
            result = {'status': 'success'}
        else:
            result = {'status': 'fail'}
        g.db.close()
        return jsonify(result)





if __name__ == "__main__":

    # #create database if it doesn't exist yet
    # if not os.path.exists(app.database):
    #     with sqlite3.connect(app.database) as connection:
    #         c = connection.cursor()
    #         c.execute("""CREATE TABLE shop_items(name TEXT, quantitiy TEXT, price TEXT)""")
    #         c.execute("""CREATE TABLE employees(username TEXT, password TEXT)""")
    #         c.execute('INSERT INTO shop_items VALUES("water", "40", "100")')
    #         c.execute('INSERT INTO shop_items VALUES("juice", "40", "110")')
    #         c.execute('INSERT INTO shop_items VALUES("candy", "100", "10")')
    #         c.execute('INSERT INTO employees VALUES("itsjasonh", "{}")'.format(hash_pass("badword")))
    #         c.execute('INSERT INTO employees VALUES("theeguy9", "{}")'.format(hash_pass("badpassword")))
    #         c.execute('INSERT INTO employees VALUES("newguy29", "{}")'.format(hash_pass("pass123")))
    #         connection.commit()
    #         connection.close()

    app.run(host='0.0.0.0') # runs on machine ip address to make it visible on netowrk