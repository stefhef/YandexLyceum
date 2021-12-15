import sqlite3

with sqlite3.connect('music_db.sqlite') as con:
    gen = input()
    cur = con.cursor()
    st = f"""SELECT DISTINCT Album.Title FROM Album
    INNER JOIN Track ON Track.AlbumId = Album.AlbumId
    INNER JOIN Genre ON Track.GenreId = Genre.GenreId
    WHERE Genre.Name='{gen}'
    ORDER BY Album.ArtistId, Album.Title"""
    data = cur.execute(st).fetchall()
    for elem in data:
        print(elem[0])
