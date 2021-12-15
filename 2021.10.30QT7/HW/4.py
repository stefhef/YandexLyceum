import sqlite3

with sqlite3.connect(input()) as con:
    cur = con.cursor()
    st = """SELECT films.title FROM films
    WHERE films.title LIKE '%Астерикс%' AND films.title NOT LIKE '%Обеликс%'"""
    data = cur.execute(st).fetchall()
    for elem in data:
        print(elem[0])
