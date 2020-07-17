#-*-coding:utf-8 -*
from categories import Categories
from products import Products
import substitutes
import database
import initialisation

class Research:

    def __init__(self):
        self.categories = Categories()
        self.products = Products()
        self.substitutes_instance = None

    def instanciate(self, database_instance):
        self.substitutes_instance = substitutes.Substitutes()

    def research(self, database_instance):
        self.products.process(self.categories)
        substitutes.Substitutes.process(self.substitutes_instance,\
        self.products)
        database.Database.insert_substitute(database_instance,\
        self.products, self.substitutes_instance)
        initialisation.Initialisation.initiate()
