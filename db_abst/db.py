import sqlite3
def db_connect(url):
        try:
            conn = sqlite3.connect(url, check_same_thread=False)
            conn.row_factory = sqlite3.Row
            return conn
        except sqlite3.OperationalError as err:
            print(f"DB connection error: {err}")
