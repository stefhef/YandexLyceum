import sqlite3

with sqlite3.connect(input()) as con:
    cur = con.cursor()
    st = """SELECT title FROM films WHERE year BETWEEN 1995 AND 2000
     AND genre=(SELECT id FROM main.genres WHERE title='детектив')"""
    data = cur.execute(st).fetchall()
    for elem in data:
        print(elem[0])
