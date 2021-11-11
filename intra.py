import db
import test

cur = db.external_db()
query = test.query()

cur.execute(query)