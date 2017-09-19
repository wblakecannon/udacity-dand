# This code attempts to insert a new row into the database, but doesn't
# commit the insertion.  Add a commit call in the right place to make
# it work properly.
# 

import sqlite3

db = sqlite3.connect("testdb")
c = db.cursor()
c.execute("insert into balloons values ('blue', 'water') ")
db.commit()
db.close()
