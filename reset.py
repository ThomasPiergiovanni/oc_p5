#-*-coding:utf-8 

from database import Database
from categories import Categories
from products import Products
import initialisation
import menu

class Reset:
    def __init__(self, database):
        self.database = database
        self.categories = Categories(self.database)
        self.products = None
        self.process()
        
    def process(self):
        self.database.download_categories()
        self.database.execute_one(self.database.delete_db())
        self.database.execute_one(self.database.create_db())
        self.database.execute_one(self.database.set_db())
        self.database.execute_one(self.categories.create_table())

        self.database.create()

        self.database.insert_categories()
        self.categories.instanciate_category()
        for category in self.categories.categories_list:
            self.database.download_products(category)
            self.database.insert_products(category)
        self.products = Products(self.database)
        menu.Menu(self.database)

