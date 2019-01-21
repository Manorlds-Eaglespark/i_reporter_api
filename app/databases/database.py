import psycopg2
import os


class Database:

    """docstring for Database class"""

    def __init__(self):
        # db_name = os.getenv("DATABASE")
        db_name = "ireporter"
        self.connection = psycopg2.connect(user="postgres", password="", host="127.0.0.1", port="5432",
                                           database=db_name)
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True