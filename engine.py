#-*-coding:utf-8 -*
"""Engine module.
"""
from admin.tests import Tests
from loop.abandon import Abandon
from loop.database import Database
from loop.categories import Categories
from loop.records import Records
from loop.products import Products
from loop.substitutes import Substitutes
from loop.menu import Menu

class Engine:
    """Engine class.
    """
    def __init__(self):
        self.tests = Tests()
        self.menu = Menu()
        self.database = Database()
        self.categories = Categories()
        self.products = Products()
        self.substitutes = Substitutes()
        self.records = Records()
        self.abandon = Abandon()
        self.initialize_database()

    def initialize_database(self):
        """Method that initialize the database. It checks if
        the DB exists and  its tables exists.
        - If it does, the program "datas" are strored into a list and the
        Menu program is started.
        - If it don't, the database and its componnents are created.
        """
        if self.database.verify(self.database.exists()):
            self.database.execute_one(self.database.use())
            if self.database.verify(self.categories.exists()) and\
            self.database.verify(self.products.exists()) and\
            self.database.verify(self.substitutes.exists()):
                if self.database.verify(self.categories.populated()) and\
                self.database.verify(self.products.populated()):
                    self.set_datas()
                    self.start_loop()
                else:
                    self.database.reset(self)
            else:
                self.database.reset(self)
        else:
            self.database.reset(self)

    def set_datas(self):
        """Method that sets datas into their
        respective list.
        """
        self.categories.set_categories_list(self.database)
        self.products.set_products_list(self.database)
        self.substitutes.set_substitutes_list(self.database)
        self.records.set_records_list(self)

    def start_loop(self):
        """Method that start the Menu loop(i.e. the main loop).
        """
        self.menu.start(self)
       