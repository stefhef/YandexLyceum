import sqlite3


def get_result(name):
    with sqlite3.connect(name) as con:
        cur = con.cursor()
        query = f"""DELETE FROM films
        where genre=(SELECT id FROM genres WHERE title='комедия')"""
        cur.execute(query)
        con.commit()
