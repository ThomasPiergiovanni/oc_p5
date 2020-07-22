#-*-coding:utf-8 -*

from categories import Categories
from products import Products
from substitutes import Substitutes
import menu

class Research:
    def __init__(self, database):
        self.categories = Categories(database)
        self.categories.instanciate()
        self.categories.process()
        self.products = Products(database)
        self.products.instanciate()
        self.products.nominal_scenario(self.categories)
        self.substitutes = Substitutes(database)
        self.substitutes.instanciate()
        self.substitutes.process(self.products)

     
