import sqlite3


def get_result(name):
    with sqlite3.connect(name) as con:
        cur = con.cursor()
        query = f"""UPDATE films
        SET duration='42'
        WHERE duration=''"""
        cur.execute(query)
        con.commit()
