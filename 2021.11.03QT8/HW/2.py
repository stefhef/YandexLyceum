import sqlite3


def get_result(name: str) -> None:
    with sqlite3.connect(name) as con:
        query = f"""
        UPDATE films
        SET duration=100
        WHERE films.genre=(SELECT genres.id FROM genres WHERE genres.title='мюзикл') AND films.duration > 100
"""
        cur = con.cursor()
        cur.execute(query)
        con.commit()
