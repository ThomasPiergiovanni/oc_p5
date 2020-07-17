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
        self.products = Products(self.categories)
        self.substitutes = Substitutes(self.products)

    def research(self, database_instance):
        # database.Database.insert_substitute(database_instance,\
        # self.products, self.substitutes_instance)
        initialisation.Initialisation.initiate()
