import sqlite3
from config import Config


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(Config.DATABASE)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def scalar(self, query, params=()):
        self.cursor.execute(query, params)
        row = self.cursor.fetchone()

        if row:
            return row[0]

        return 0

    def query(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()