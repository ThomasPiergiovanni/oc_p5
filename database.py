#-*-coding:utf-8 -*
import requests

import mysql.connector

import config

class Database:
    def __init__(self): 
        self.connection = mysql.connector.connect\
        (host = config.HOST, user = config.USER,\
        password = config.PASSWORD)
        self.para1 = None
        self.para2 = None
        self.status = False
        self.source= {}

    def create(self):
        statement = "CREATE DATABASE IF NOT EXISTS %s CHARACTER\
        SET 'utf8';"% config.DATABASE_NAME
        return statement

    def delete(self):
        statement = "DROP DATABASE IF EXISTS %s"% config.DATABASE_NAME
        return statement


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

    def use(self):
        statement = "USE %s"% config.DATABASE_NAME
        return statement
        
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

    def verify (self, para1, para2):
        try:
            self.open_cursor()
            self.cursor.execute(para1)
            self.cursor.fetchall()
            if self.cursor.rowcount >= 1:
                self.status = True
            self.close_cursor()
        except:
            self.status = False
            print(para2)

    def exists(self):
        self.para1 = "SHOW DATABASES LIKE '%s'"% config.DATABASE_NAME
        self.para2 = "No DB"

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


