# -*-coding:utf-8 -*
"""Connection manager module.
"""
from sys import exit as leave_program

import requests
import mysql.connector

from configuration.config import CATEGORIES_ENDPOINT, HEADER
from configuration.env import HOST, USER, PASSWORD, DATABASE_NAME
from models.mapper.category import Category
from models.mapper.product import Product
from models.mapper.record import Record
from models.mapper.substitute import Substitute


class ConnectionManager:
    """Database class.
    """
    def __init__(self):
        self.engine = None
        self.categories = None
        self.products = None
        self.substitutes = None
        self.connection = mysql.connector.connect(
            host=HOST, user=USER,
            password=PASSWORD)
        self.cursor = None
        self.status = False

    def download(self, engine, parameters):
        """Method that makes a parameterized request to OFF API (provided
        by categories and products modules methods).
        """
        try:
            self.engine = engine
            response_api = requests.get(
                parameters[0], headers=HEADER,
                params=parameters[1])
            if parameters[0] == CATEGORIES_ENDPOINT:
                self.categories = engine.categories
                self.categories.source = response_api.json()
            else:
                self.products = engine.products
                self.products.source = response_api.json()
        except requests.ConnectionError:
            print(
                "Un problème de connection est apparu. Ré-essaayez plus"
                " tard ou contacter le propriétaire de l'application")
            leave_program()
        except requests.Timeout:
            print(
                "Un problème de connection est apparu. Ré-essaayez plus"
                " tard ou contacter le propriétaire de l'application")
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

    def set_categories_list(self, engine, parameters):
        self.engine = engine
        self.categories = engine.categories
        self.categories.categories_list.clear()
        self.open_cursor()
        self.cursor.execute(parameters[0])
        selection = self.cursor.fetchall()
        for elt in selection:
            category = Category(
                elt[0], elt[1], elt[2], elt[3])
            self.categories.categories_list.append(category)
        self.close_cursor()

    def set_products_list(self, engine, parameters):
        """Method that create the products' list.
        """
        self.engine = engine
        self.products = engine.products
        self.products.products_list.clear()
        self.open_cursor()
        self.cursor.execute(parameters[0])
        selection = self.cursor.fetchall()
        for elt in selection:
            product = Product(
                elt[0], elt[1], elt[2], elt[3], elt[4], elt[5], elt[6])
            self.products.products_list.append(product)
        self.close_cursor()

    def set_substitutes_list(self, engine, parameters):
        """Method that create the substitutes' list.
        """
        self.engine = engine
        self.substitutes = engine.substitutes
        self.substitutes.substitutes_list.clear()
        self.open_cursor()
        self.cursor.execute(parameters[0])
        selection = self.cursor.fetchall()
        for elt in selection:
            substitute = Substitute(elt[0], elt[1])
            self.substitutes.substitutes_list.append(substitute)
        self.close_cursor()
