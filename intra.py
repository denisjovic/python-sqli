import db
import source

def intra_function():
    cur = db.external_db()
    query = source.query()

    cur.execute(query)

intra_function()