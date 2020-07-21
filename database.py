#-*-coding:utf-8 -*
import requests

import mysql.connector

import config

class Database:
    def __init__(self): 
        self.connection = mysql.connector.connect\
        (host = config.HOST, user = config.USER,\
        password = config.PASSWORD)
        self.status = False
        self.statement = None
        self.source= {}


    def download(self, endpoint, parameters):
        try:
            response_api =requests.get(endpoint,\
            headers = config.HEADER, params = parameters)
            self.source = response_api.json()
        except requests.HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
        except Exception as other_error:
            print(f"Other error occurred: {other_error}")
        else:
            print("HTTP call to API successfull")

    def set_db(self):
        self.statement = "USE %s"% config.DATABASE_NAME
        return self.statement
        
    def close_connection_to_db(self):
        self.connection.close()

    def open_cursor(self):
        self.cursor = self.connection.cursor()

    def close_cursor(self):
        self.cursor.close()

    def execute_one(self, statement):
        self.open_cursor()
        self.cursor.execute(statement)
        self.connection.commit()
        self.close_cursor()

    def execute_many(self, statement, values):
        self.open_cursor()
        self.cursor.executemany(statement, values)
        self.connection.commit()
        self.close_cursor()

    def exists(self):
        try:
            self.open_cursor()
            self.cursor.execute("SHOW DATABASES LIKE '%s'"% config.DATABASE_NAME)
            self.cursor.fetchall()
            if self.cursor.rowcount >= 1:
                self.status = True
            self.close_cursor()
        except:
            self.status = False
            print("No DB")

    def content(self):
        querries = ("category","product")
        try: 
            for querry in querries:
                self.open_cursor()
                self.cursor.execute("SELECT * FROM %s"% querry)
                self.cursor.fetchall()
                if self.cursor.rowcount >= 1:
                    self.status = True
                self.close_cursor()
        except:
            self.status = False
            print ("No or empty tables")

    def create_db(self):
        statement = "CREATE DATABASE IF NOT EXISTS %s CHARACTER\
        SET 'utf8';"% config.DATABASE_NAME
        return statement

    def delete_db(self):
        statement = "DROP DATABASE IF EXISTS %s"% config.DATABASE_NAME
        return statement
