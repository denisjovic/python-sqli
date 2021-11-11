import db

username = input('Enter username')

cur = db.external_db()

cur.execute("SELECT * FROM employees WHERE username = '%s' " %(username))
cur.commit()
cur.close()