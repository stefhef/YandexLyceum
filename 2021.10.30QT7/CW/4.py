import sqlite3

with sqlite3.connect(input()) as con:
    cur = con.cursor()
    st = f"""SELECT films.title FROM films WHERE films.duration >= 60 AND
     films.genre = (SELECT id FROM main.genres WHERE title = 'комедия')"""
    data = cur.execute(st).fetchall()
    for elem in data:
        print(elem[0])
