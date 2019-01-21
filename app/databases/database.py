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
                                   "registered TIMESTAMP NOT NULL)")
        sql_command_incidents_table = ("CREATE TABLE IF NOT EXISTS incidents"
                                       "(id SERIAL PRIMARY KEY,"
                                       "created_on TIMESTAMP NOT NULL,"
                                       "created_by INTEGER NOT NULL,"
                                       "type TEXT NULL,"
                                       "location TEXT NOT NULL,"
                                       "status TEXT NOT NULL,"
                                       "images TEXT NOT NULL,"
                                       "videos TEXT NOT NULL,"
                                       "comment TEXT NOT NULL)")
        self.cursor.execute(sql_command_users_table)
        self.cursor.execute(sql_command_incidents_table)
        self.cursor.connection.commit()

    def save_user(self, user):
        postgres_insert_user_query = ("INSERT INTO users ("
                                          "firstname, lastname, othernames, email, password,"
                                          "phonenumber, username, isadmin, registered) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id")
        record_to_insert = (user.firstname, user.lastname, user.othernames, user.email, user.password, user.phonenumber, user.username, user.isadmin, user.registered)
        self.cursor.execute(postgres_insert_user_query, record_to_insert)
        user_id = self.cursor.fetchone()
        return user_id

    def get_user_by_email(self, email):
        postgresql_select_user_query = """SELECT * FROM users where email = '{0}' """.format(email)
        self.cursor.execute(postgresql_select_user_query)
        user = self.cursor.fetchone()
        return user


    def delete_all_tables(self):
            sql_clean_command_users_table = "TRUNCATE TABLE users RESTART IDENTITY CASCADE"
            sql_clean_command_incidents_table = "TRUNCATE TABLE incidents RESTART IDENTITY CASCADE"
            self.cursor.execute(sql_clean_command_users_table)
            self.cursor.execute(sql_clean_command_incidents_table)
