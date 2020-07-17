#-*-coding:utf-8 -*
from categories import Categories
from products import Products
from substitutes import Substitutes
import substitutes
import database
import initialisation

class Research:

    def __init__(self):
        self.categories = Categories()
        self.products = Products()
        self.substitutes = Substitutes()

    def research(self, database_instance):
        self.products.process(self.categories)
        self.substitutes.process(self.products)
        database.Database.insert_substitute(database_instance,\
        self.products, self.substitutes_instance)
        initialisation.Initialisation.initiate()
