#-*-coding:utf-8 -*
from categories import Categories
import products
import substitutes
import database
import initialisation

class Research:

    def __init__(self):
        self.categories = Categories()
        self.products_instance = None
        self.substitutes_instance = None


    def instanciate(self, database_instance):
        self.products_instance = products.Products()
        products.Products.instanciate_product(self.products_instance,\
        database_instance)
        self.substitutes_instance = substitutes.Substitutes()

    def research(self, database_instance):
        self.categories.process()
        products.Products.process(self.products_instance,\
        self.categories)
        substitutes.Substitutes.process(self.substitutes_instance,\
        self.products_instance)
        database.Database.insert_substitute(database_instance,\
        self.products_instance, self.substitutes_instance)
        initialisation.Initialisation.initiate()
