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
        self.products = Products(self.database)
        self.substitutes = Substitutes (self.database)
        self.reset_database()
        self.reset_categories()
        self.reset_products()
        self.reset_substitutes()
        menu.Menu(self.database)
        
    def reset_database(self):
        self.database.execute_one(self.database.delete())
        self.database.execute_one(self.database.create())
        self.database.execute_one(self.database.use())

    def reset_categories(self):
        endpoint, parameters = self.categories.source()
        self.database.download(endpoint, parameters)
        self.database.execute_one(self.categories.create_table())
        self.categories.insert_in_table()
        self.database.execute_many(self.categories.statement,\
        self.categories.values)
        self.categories.instanciate()

    def reset_products(self):
        self.database.execute_one(self.products.create_table())
        for category in self.categories.categories_list:
            endpoint, parameters = self.products.source(category)
            self.database.download(endpoint, parameters)
            self.database.execute_one(self.products.create_table())
            statement, values = self.products.insert_in_table(category)
            self.database.execute_many(statement, values)
        self.products.instanciate()

    def reset_substitutes(self):
        self.database.execute_one(self.substitutes.create_table())


        

