#-*-coding:utf-8 -*
"""Engine module.
"""
from programm.admin.database import Database
from programm.admin.tests import Tests
from programm.content.categories import Categories
from programm.content.products import Products
from programm.content.substitutes import Substitutes
from programm.content.compositions import Compositions
from programm.structure import menu
# from programm.structure.reset import Reset

class Engin:
    """Engin class.
    """
    def __init__(self):
        self.database = Database()
        self.tests = Tests()
        self.menu = menu.Menu()
        self.categories = Categories()
        self.products = Products()
        self.substitutes = Substitutes()
        self.compositions = Compositions()
        self.initialize_database()

    def initialize_database(self):
        """Method that initialize the database. If it exist, 
        the programm continues. If it doesn't, the database 
        and its componnent are created.
        """
        if self.database.verify(self.database.exists()):
            self.initialize_datas()
        else:
            Reset(self.database)


    def initialize_datas(self):
        """Method that initialize the database datas. If they exist, 
        the programm continues. If they don't, the database is droped
        and recreated along with the datas.
        """
        self.database.execute_one(self.database.use())
        if self.database.verify(self.categories.exists()) and\
        self.database.verify(self.products.exists()):
            self.categories.instanciate(self.database)
            self.products.instanciate(self.database)
            self.substitutes.instanciate(self.database)
            self.compositions.instanciate(self.categories, self.products,\
            self.substitutes)
            self.start_loops()
            

        else:
            print("bug")
            pass
            # Reset(self.database)

    def start_loops(self):
        """Method that initiate the programm loops..
        """
        self.menu.menu_nominal_scenario(self.database, self.tests,\
        self.categories, self.products, self.substitutes,\
        self.compositions)

        