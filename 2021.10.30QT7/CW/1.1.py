import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result1 = cur.execute("""SELECT films.title FROM films WHERE films.year > 1996 AND films.genre=7""").fetchall()
result2 = cur.execute("""SELECT films.title FROM films WHERE films.year > 1996 AND films.genre=9""").fetchall()
for elem in result1:
    print(elem[0])
for elem in result2:
    print(elem[0])
con.close()
