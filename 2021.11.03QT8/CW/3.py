import sqlite3


def get_result(name):
    with sqlite3.connect(name) as con:
        cur = con.cursor()
        query = f"""UPDATE films
        SET duration = duration * 2
        WHERE genre=(SELECT id FROM genres WHERE genres.title='фантастика')"""
        cur.execute(query)
        con.commit()
