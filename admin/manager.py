#-*-coding:utf-8 -*
"""Manager module.
"""
from sys import exit as leave_program

import requests
import mysql.connector

from admin.config import HEADER
from admin.env import HOST, USER, PASSWORD, DATABASE_NAME

class Manager:
    """Manager class.
    """
    def __init__(self):
        self.engine = None
        self.source = {}
        self.connection = mysql.connector.connect\
        (host=HOST, user=USER, password=PASSWORD)
        self.cursor = None
        self.status = False

    def download(self, parameters):
        """Method that makes a parameterized (provided
        by categories and products modules methods) request to OFF API.
        """
        try:
            response_api = requests.get(parameters[0],\
            headers=HEADER, params=parameters[1])
            self.source = response_api.json()
        except requests.ConnectionError as cnx_error:
            print("A connection error occured. Please try later or \
contact APP owner")
            leave_program()
        except requests.Timeout as tmo_error:
            print("A connectionn timeout error occured. Please try later or\
contact APP owner")
            leave_program()



    def open_cursor(self):
        """Method that open a connection cursor.
        """
        self.cursor = self.connection.cursor()

    def close_cursor(self):
        """Method that close a connection cursor.
        """
        self.cursor.close()

    def execute_one(self, parameters):
        """Method that execute a sql statement (provided
        by various modules methods) once.
        """
        self.open_cursor()
        self.cursor.execute(parameters[0], parameters[1])
        self.connection.commit()
        self.close_cursor()

    def execute_many(self, parameters):
        """Method that execute a sql statement (provided
        by various modules methods) multiple times.
        """
        self.open_cursor()
        self.cursor.executemany(parameters[0], parameters[1])
        self.connection.commit()
        self.close_cursor()

    def verify(self, parameters):
        """Method that verify the truth of a given sql statement (provided
        by various modules methods) and returns a boolean.
        """
        self.open_cursor()
        self.cursor.execute(parameters[0])
        self.cursor.fetchall()
        if self.cursor.rowcount >= 1:
            self.status = True
        else:
            self.status = False
        self.close_cursor()
        return self.status