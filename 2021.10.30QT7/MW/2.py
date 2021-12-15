import sqlite3

with sqlite3.connect('music_db.sqlite') as con:
    gen = input()
    cur = con.cursor()
    artists = set()
    query = f"""SELECT TrackId FROM Track
    WHERE Track.GenreId = (SELECT GenreId FROM Genre
    WHERE Genre.Name='{gen}')"""
    tr_id = cur.execute(query).fetchall()
    for ti in tr_id:
        query = f"""SELECT DISTINCT Album.AlbumId FROM Album
        INNER JOIN Track ON Track.AlbumId = Album.AlbumId
        WHERE TrackId={ti[0]}"""

        albums_id = cur.execute(query).fetchall()
        for id in albums_id:
            query = f"""SELECT DISTINCT Artist.Name FROM Artist
            INNER JOIN Album ON Artist.ArtistId = Album.ArtistId
            WHERE Album.AlbumId={id[0]}"""
            data = cur.execute(query).fetchall()
            for art in data:
                artists.add(art[0])
    for elem in sorted(artists):
        print(elem[0])
