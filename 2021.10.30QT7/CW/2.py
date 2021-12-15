import sqlite3

with sqlite3.connect(input()) as con:
    cur = con.cursor()
    st = """SELECT title FROM films WHERE title like '%?'"""
    for elem in cur.execute(st).fetchall():
        print(elem[0])
