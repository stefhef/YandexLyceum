import sqlite3

with sqlite3.connect('music_db.sqlite') as con:
    gen = input()
    cur = con.cursor()
    query = f"""SELECT DISTINCT Artist.Name FROM Artist
    INNER JOIN Album ON Artist.ArtistId = Album.ArtistId
    INNER JOIN Track ON Track.AlbumId = Album.AlbumId
    INNER JOIN Genre ON Track.GenreId = Genre.GenreId
    WHERE Genre.Name='{gen}'
    ORDER BY Artist.Name"""
    data = cur.execute(query).fetchall()
    for elem in data:
        print(elem[0])
