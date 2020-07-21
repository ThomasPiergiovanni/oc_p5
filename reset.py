#-*-coding:utf-8 

from database import Database
from categories import Categories
from products import Products
from substitutes import Substitutes
import initialisation
import menu

class Reset:
    def __init__(self, database):
        self.database = database
        self.categories = Categories(self.database)
        self.products = Products(self.database)
        self.substitutes = Substitutes (self.database)
        self.process()
        
    def process(self):
        endpoint, parameters = self.categories.source()
        self.database.download(endpoint, parameters)
        self.database.execute_one(self.database.delete_db())
        self.database.execute_one(self.database.create_db())
        self.database.execute_one(self.database.set_db())

        self.database.execute_one(self.categories.create_table())
        self.database.execute_one(self.products.create_table())
        self.database.execute_one(self.substitutes.create_table())

        self.database.insert_categories()
        self.categories.instanciate_category()
        for category in self.categories.categories_list:
            endpoint, parameters = self.products.source(category)
            self.database.download(endpoint, parameters)
            self.database.insert_products(category)
        self.products = Products(self.database)
        self.products.instanciate_product()
        menu.Menu(self.database)

