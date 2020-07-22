#-*-coding:utf-8 -*

from categories import Categories
from products import Products
from substitutes import Substitutes
from compositions import Compositions


class Record:
    def __init__(self, database):
        self.categories = Categories(database)
        self.categories.instanciate()
        self.products = Products(self.categories)
        self.products.instanciate()
        self.substitutes = Substitutes(self.products)
        self.substitutes.instanciate()
        Compositions(self.categories, self.products, self.substitutes, database)
