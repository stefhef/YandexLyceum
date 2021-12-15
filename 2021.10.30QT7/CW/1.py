import sqlite3

with sqlite3.connect(input()) as con:
    cur = con.cursor()
    st = f"""SELECT films.title FROM films WHERE films.year >= 1997 AND films.genre
     IN (SELECT id FROM main.genres WHERE title in ('музыка', 'анимация'))"""
    data = cur.execute(st).fetchall()
    for elem in data:
        print(elem[0])
