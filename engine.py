#-*-coding:utf-8 -*
"""Engine module.
"""
from admin.manager import Manager
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
        self.manager = Manager()
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
        if self.manager.verify(self.database.exists()):
            self.manager.execute_one(self.database.use())
            if self.manager.verify(self.categories.exists()) and\
            self.manager.verify(self.products.exists()) and\
            self.manager.verify(self.substitutes.exists()):
                if self.manager.verify(self.categories.populated()) and\
                self.manager.verify(self.products.populated()):
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
        self.categories.set_categories_list(self.manager)
        self.products.set_products_list(self.manager)
        self.substitutes.set_substitutes_list(self.manager)
        self.records.set_records_list(self)

    def start_loop(self):
        """Method that start the Menu loop(i.e. the main loop).
        """
        self.menu.start(self)
       