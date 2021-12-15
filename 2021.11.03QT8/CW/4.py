import sqlite3


def get_result(name):
    with sqlite3.connect(name) as con:
        cur = con.cursor()
        query = f"""DELETE FROM films
        WHERE title LIKE 'Я%а'"""
        cur.execute(query)
        con.commit()
