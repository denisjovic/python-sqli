import db

username = input('Enter username')

cur = db.external_db()

cur.execute(f'SELECT * FROM users WHERE username = ${username}')
cur.commit()
cur.close()