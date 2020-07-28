#-*-coding:utf-8 -*
"""Engine module.
"""
from programm.admin.database import Database
from programm.admin.tests import Tests
from programm.loop.menu import Menu
from programm.loop.loops.abandon import Abandon
from programm.loop.loops.categories import Categories
from programm.loop.loops.records import Records
from programm.loop.loops.products import Products
from programm.loop.loops.substitutes import Substitutes


class Engin:
    """Engin class.
    """
    def __init__(self):
        self.database = Database()
        self.tests = Tests()
        # self.menu = menu.Menu()
        self.menu = Menu()
        self.categories = Categories()
        self.products = Products()
        self.substitutes = Substitutes()
        self.records = Records()
        self.abandon = Abandon()

    def initialize_database(self):
        """Method that initialize the database. If it exist, 
        the programm continues. If it doesn't, the database 
        and its componnent are created.
        """
        if self.database.verify(self.database.exists()):
            self.initialize_datas()
        else:
            self.database.reset(self)


    def initialize_datas(self):
        """Method that initialize the database datas. If they exist, 
        the programm continues. If they don't, the database is droped
        and recreated along with the datas.
        """
        self.database.execute_one(self.database.use())
        if self.database.verify(self.categories.exists()) and\
        self.database.verify(self.products.exists()):
            self.categories.set_categories_list(self.database)
            self.products.set_products_list(self.database)
            self.substitutes.set_substitutes_list(self.database)
            self.records.set_records_list(self)
            self.start_loops()
            
        else:
            print("bug")
            self.database.reset(self)

    def refresh_datas(self):
        self.categories.set_categories_list(self.database)
        self.products.set_products_list(self.database)
        self.substitutes.set_substitutes_list(self.database)
        self.records.set_records_list(self)

    def start_loops(self):
        """Method that initiate the programm loops..
        """
        self.menu.start_menu(self)

        