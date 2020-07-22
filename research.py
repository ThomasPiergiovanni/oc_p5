#-*-coding:utf-8 -*

from categories import Categories
from products import Products
from substitutes import Substitutes
import menu

class Research:
    def __init__(self, database):
        self.database = database
        self.categories = Categories(self.database)
        self.categories.research_nominal_scenario()
        self.products = Products(self.categories)
        self.products.research_nominal_scenario()
        self.substitutes = Substitutes(self.products)
        self.substitutes.instanciate()
        self.substitutes.nominal_scenario()

     
