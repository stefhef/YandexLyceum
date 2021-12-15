import sqlite3


def get_result(name: str) -> None:
    with sqlite3.connect(name) as con:
        query = f"""
        UPDATE films
        SET duration= duration / 3
        WHERE films.year=1973
"""
        cur = con.cursor()
        cur.execute(query)
        con.commit()
