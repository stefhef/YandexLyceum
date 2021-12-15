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
        query = f"""SELECT Album.AlbumId FROM Album
        WHERE Album.AlbumId = (SELECT AlbumId FROM Track WHERE TrackId={ti[0]})"""

        albums_id = cur.execute(query).fetchall()
        for id in albums_id:
            query = f"""SELECT DISTINCT Artist.Name FROM Artist
            WHERE Artist.ArtistId = (SELECT ArtistId FROM Album WHERE Album.AlbumId={id[0]})"""
            data = cur.execute(query).fetchall()
            for art in data:
                artists.add(art[0])
    for elem in sorted(artists):
        print(elem[0])
