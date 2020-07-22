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
        self.source= {}

    def reset_nominal_scenario(self):
        self.execute_one(self.delete())
        self.execute_one(self.create())
        self.execute_one(self.use())

    def create(self):
        statement = "CREATE DATABASE IF NOT EXISTS %s CHARACTER\
        SET 'utf8';"% config.DATABASE_NAME
        parameters =[statement, None]
        return parameters

    def delete(self):
        statement = "DROP DATABASE IF EXISTS %s"% config.DATABASE_NAME
        parameters =[statement, None]
        return parameters

    def download(self, parameters):
        try:
            response_api =requests.get(parameters[0],\
            headers = config.HEADER, params = parameters[1])
            self.source = response_api.json()
        except requests.HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
        except Exception as other_error:
            print(f"Other error occurred: {other_error}")
        else:
            print("HTTP call to API successfull")

    def use(self):
        statement = "USE %s"% config.DATABASE_NAME
        parameters =[statement, None]
        return parameters
        
    def close_connection_to_db(self):
        self.connection.close()

    def open_cursor(self):
        self.cursor = self.connection.cursor()

    def close_cursor(self):
        self.cursor.close()

    def execute_one(self, parameters):
        self.open_cursor()
        self.cursor.execute(parameters[0], parameters[1])
        self.connection.commit()
        self.close_cursor()

    def execute_many(self, parameters):
        self.open_cursor()
        self.cursor.executemany(parameters[0], parameters[1])
        self.connection.commit()
        self.close_cursor()

    def verify(self, parameters):
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

    def exists(self):
        statement = "SHOW DATABASES LIKE '%s'"% config.DATABASE_NAME
        message= "No DB"
        parameters = [statement, message]
        return parameters




