import sqlite3

with sqlite3.connect(input()) as con:
    cur = con.cursor()
    st = """SELECT films.title FROM films
    WHERE films.duration < 86"""
    data = cur.execute(st).fetchall()
    for elem in data:
        print(elem[0])
