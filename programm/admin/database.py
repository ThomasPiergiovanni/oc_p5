#-*-coding:utf-8 -*
"""Database module.
"""
import requests
import mysql.connector

from programm.admin import config

class Database:
    """Database class.
    """
    def __init__(self):
        self.connection = mysql.connector.connect\
        (host=config.HOST, user=config.USER, password=config.PASSWORD)
        self.cursor = None
        self.status = False
        self.source = {}

    def reset(self, engin):
        """Method that starts the database reset
        nominal scenario.
        """
        self.engin = engin
        self.categories = engin.categories
        self.execute_one(self.delete())
        self.execute_one(self.create())
        self.execute_one(self.use())
        self.categories.reset(self.engin)

    def verify(self, parameters):
        """Method that verify the truth of an sql statement.
        """
        try:
            self.open_cursor()
            self.cursor.execute(parameters[0])
            self.cursor.fetchall()
            if self.cursor.rowcount >= 1:
                self.status = True
            self.close_cursor()
        except:
            self.status = False
            print(parameters[1])

        return self.status

    def exists(self):
        """Method that provides the sql statement and
        message for database verification.
        """
        statement = "SHOW DATABASES LIKE '%s'"% config.DATABASE_NAME
        message = "No DB"
        parameters = [statement, message]
        return parameters

    def delete(self):
        """Method that provides the sql statement for
        database deletion.
        """
        statement = "DROP DATABASE IF EXISTS %s"% config.DATABASE_NAME
        parameters = [statement, None]
        return parameters

    def create(self):
        """Method that provides the sql statement for
        database creation.
        """
        statement = "CREATE DATABASE IF NOT EXISTS %s CHARACTER\
        SET 'utf8';"% config.DATABASE_NAME
        parameters = [statement, None]
        return parameters

    def download(self, parameters):
        """Method that get the parameterized data from the API.
        """
        try:
            response_api = requests.get(parameters[0],\
            headers=config.HEADER, params=parameters[1])
            self.source = response_api.json()
        except requests.HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
        except Exception as other_error:
            print(f"Other error occurred: {other_error}")
        else:
            print("HTTP call to API successfull")

    def use(self):
        """Method that gives the appropriate database to use for
        the program.
        """
        statement = "USE %s"% config.DATABASE_NAME
        parameters = [statement, None]
        return parameters

    def close_connection_to_db(self):
        """Method that close the connection to the database.
        """
        self.connection.close()

    def open_cursor(self):
        """Method that open a connection cursor.
        """
        self.cursor = self.connection.cursor()

    def close_cursor(self):
        """Method that close a connection cursor.
        """
        self.cursor.close()

    def execute_one(self, parameters):
        """Method that execute a sql statement once.
        """
        self.open_cursor()
        self.cursor.execute(parameters[0], parameters[1])
        self.connection.commit()
        self.close_cursor()

    def execute_many(self, parameters):
        """Method that execute a sql statement multiple times.
        """
        self.open_cursor()
        self.cursor.executemany(parameters[0], parameters[1])
        self.connection.commit()
        self.close_cursor()
