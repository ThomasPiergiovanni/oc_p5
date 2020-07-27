#-*-coding:utf-8 -*
"""Engine module.
"""
from programm.admin.database import Database
from programm.content.categories import Categories
from programm.content.products import Products
from programm.structure import menu
from programm.structure.reset import Reset

class Engin:
    """Engin class.
    """
    def __init__(self):
        self.initialize_database()

    def initialize_database(self):
        """Method that initialize the database. If it exist, 
        the programm continues. If it doesn't, the database 
        and its componnent are created.
        """
        self.database = Database()
        if self.database.verify(self.database.exists()):
            self.initialize_datas()
        else:
            Reset(self.database)


    def initialize_datas(self):
        """Method that initialize the database datas. If they exist, 
        the programm continues. If they don't, the database is droped
        and recreated along with the datas.
        """
        self.categories = Categories(self.database)
        self.products = Products(self.categories)
        self.database.execute_one(self.database.use())
        if self.database.verify(self.categories.exists()) and\
        self.database.verify(self.products.exists()):
            self.start_loops()
        else:
            Reset(self.database)

    def start_loops(self):
        """Method that initiate the programm loops..
        """
        self.menu = menu.Menu(self.database)
        self.menu.menu_nominal_scenario()
        