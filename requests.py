import requests
import db

req = requests.get('http://localhost.com/users/:id')

user_id = req.text

cur = db.external_db()

cur.execute(f'SELECT * FROM users WHERE id = ${user_id}')
cur.commit()
cur.close()


