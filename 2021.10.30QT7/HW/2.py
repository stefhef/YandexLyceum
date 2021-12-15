import sqlite3

with sqlite3.connect(input()) as con:
    cur = con.cursor()
    st = """SELECT DISTINCT genres.title FROM films
    INNER JOIN genres ON films.genre = genres.id
    WHERE year BETWEEN 2010 AND 2011"""
    data = cur.execute(st).fetchall()
    for elem in data:
        print(elem[0])
