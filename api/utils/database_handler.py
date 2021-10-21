import sqlite3
from config import DATABASE_FILENAME 


conn = sqlite3.connect(DATABASE_FILENAME)
cur = conn.cursor()


def execute_command(command):
    cur.execute(command)


conn.close()

