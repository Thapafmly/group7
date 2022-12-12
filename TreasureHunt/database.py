import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='flight_game',
            user='root',
            password='root@123',
            autocommit=True
        )

    def get_conn(self):
        return self.conn
