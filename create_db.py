import sqlite3

db_locale='student.db'

connie = sqlite3.connect(db_locale)

c = connie.cursor()

c.execute("""

CREATE TABLE contact_details 

(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER

)


""")

connie.commit()
connie.close()
