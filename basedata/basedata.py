import sqlite3

db = sqlite3.connect('helper.db')

# create cursor
c = db.cursor()

# c.execute("""CREATE TABLE articles (
#           title text,
#           full_text text,
#           views integer,
#           avtor text
# )""")
# db.commit()

# додавання даних
# c.execute("INSERT INTO articles VALUES ('Facebook is cool!', 'Facebook is really cool', 40, 'Modest')")

# виброка даних
c.execute("SELECT rowid, * FROM articles WHERE")
items = c.fetchall()
# print(c.fetchmany(1))
# print(c.fetchone()[1])

for el in items:
    print(el[1] + "\n" + el[4])

db.commit()

db.close()