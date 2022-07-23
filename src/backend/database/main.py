import psycopg2 as pg
import os


def querySet(query, values):
    try:
        conn = pg.connect(
            dbname="stocksim", password=os.environ["DATABASE_PASSWORD"], user="postgres", host="localhost"
        )
        cur = conn.cursor()
        cur.execute(query, values)
        conn.commit()
        cur.close()
        conn.close()
    except:
        raise Exception("Internal error")


def queryGet(query, values=()):
    try:
        conn = pg.connect(
            dbname="stocksim", password=os.environ["DATABASE_PASSWORD"], user="postgres", host="localhost"
        )
        cur = conn.cursor()
        cur.execute(query, values)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except:
        raise Exception("Internal error")
