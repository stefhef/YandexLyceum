import sqlite3


def get_result(name: str) -> None:
    with sqlite3.connect(name) as con:
        query = f"""
        DELETE FROM films
        WHERE films.year<2000 AND films.genre=(SELECT genres.id FROM genres WHERE genres.title='фантастика')
         AND films.duration > 90
"""
        cur = con.cursor()
        cur.execute(query)
        con.commit()
