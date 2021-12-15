import sqlite3

with sqlite3.connect(input()) as con:
    cur = con.cursor()
    data = cur.execute("""SELECT DISTINCT year FROM films WHERE title like 'Х%'""")
    for elem in data:
        print(elem[0])
