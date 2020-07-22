#-*-coding:utf-8 

from categories import Categories
from products import Products
from substitutes import Substitutes
import initialisation
import menu

class Reset:
    def __init__(self, database):
        self.database = database
        self.categories = Categories(self.database)
        self.products = Products(self.categories)
        self.substitutes = Substitutes (self.products)
        self.database.reset_nominal_scenario()
        self.categories.reset_nominal_scenario()
        self.reset_products()
        self.reset_substitutes()
        menu.Menu(self.database)
        
    def reset_products(self):
        self.database.execute_one(self.products.create_table())
        for category in self.categories.categories_list:
            self.database.download(self.products.source(category))
            self.database.execute_one(self.products.create_table())
            self.database.execute_many(self.products.insert_in_table(category))
        # self.products.instanciate()

    def reset_substitutes(self):
        self.database.execute_one(self.substitutes.create_table())


        

