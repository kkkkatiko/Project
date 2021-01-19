import sqlite3

#легкий
con = sqlite3.connect("easy.sqlite")
cur = con.cursor()
x = #время
cur.execute("""INSERT INTO easy VALUES(?)""", (x,))
con.commit()

#средний
con = sqlite3.connect("medium.sqlite")
cur = con.cursor()
x = #время
cur.execute("""INSERT INTO easy VALUES(?)""", (x,))
con.commit()

#сложный
con = sqlite3.connect("hard.sqlite")
cur = con.cursor()
x = #время
cur.execute("""INSERT INTO easy VALUES(?)""", (x,))
con.commit()
