# -------------------- Connection.py --------------------
import mysql.connector as sql

def connection():
    mydb = sql.connect(
            host="localhost",
            user="root",
            password="",
            database="portfolio"
        )

    return mydb
