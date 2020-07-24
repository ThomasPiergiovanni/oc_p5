#-*-coding:utf-8 -*
"""Initialization module.
"""
from database import Database
from categories import Categories
from products import Products
from menu import Menu
from reset import Reset

class Initialization:
    """Initialization class.
    """
    def __init__(self):
        self.database = Database()
        self.categories = Categories(self.database)
        self.products = Products(self.categories)
        self.menu = Menu(self.database)

    def initialization_nominal_scenario(self):
        """Method that starts the programm initialization
        nominal scenario.
        """
        self.database.initialization_nominal_scenario()
        self.categories.initialization_nominal_scenario()
        self.products.initialization_nominal_scenario()
        if self.database.status:
            self.menu.menu_nominal_scenario()
        else:
            self.initialization_exception_scenario()

    def initialization_exception_scenario(self):
        """Method that starts the programm initialization
        exception senario.
        """
        Reset(self.database)
        