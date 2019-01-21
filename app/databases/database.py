import psycopg2
import os


class Database:

    """docstring for Database class"""

    def __init__(self):
        self.connection = psycopg2.connect(user="postgres", password="", host="127.0.0.1", port="5432",
                                           database="ireporter")
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True

    def create_all_tables(self):
        sql_command_users_table = ("CREATE TABLE IF NOT EXISTS users"
                                   "(id SERIAL PRIMARY KEY,"
                                   "firstname TEXT NOT NULL,"
                                   "lastname TEXT NOT NULL,"
                                   "othernames TEXT NULL,"
                                   "email TEXT NOT NULL,"
                                   "password TEXT NOT NULL,"
                                   "phonenumber TEXT NOT NULL,"
                                   "username TEXT NOT NULL,"
                                   "isadmin TEXT NOT NULL,"
