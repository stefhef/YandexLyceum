import sqlite3

with sqlite3.connect('music_db.sqlite') as con:
    artist = input()
    traks = set()
    cur = con.cursor()
    artist = cur.execute(f"SELECT ArtistId FROM Artist WHERE Name='{artist}'").fetchone()
    albums = cur.execute(f"""SELECT albumid FROM Album WHERE artistid={artist[0]}""").fetchall()
    for album in albums:
        tr = cur.execute(f"SELECT DISTINCT name FROM Track WHERE albumid={album[0]}").fetchall()
        for elem in tr:
            traks.add(elem[0])

for tr in sorted(traks):
    print(tr)
