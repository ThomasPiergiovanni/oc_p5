#-*-coding:utf-8 

from database import Database
from download import Download
from categories import Categories
from products import Products
import initialisation
import menu

class Reset:
    def __init__(self, database):
        self.database = database
        self.download = Download()
        self.categories = None
        self.products = None
        # self.process()
        

    def process(self):
        statement = self.database.delete_db()
        self.database.execute_one(statement)
        statement = self.database.create_db()
        self.database.execute_one(statement)
        self.database.connection_to_db()
        self.database.create()
        self.download.categories()
        self.database.insert_categories(self.download)
        self.categories = Categories(self.database)
        for category in self.categories.categories_list:
            self.download.products(category)
            self.database.insert_products(category, self.download)
        self.products = Products(self.database)
        menu.Menu(self.database)

