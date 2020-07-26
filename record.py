#-*-coding:utf-8 -*
"""Record module.
"""
from programm.content.categories import Categories
from programm.content.products import Products
from programm.content.substitutes import Substitutes
from programm.content.compositions import Compositions


class Record:
    """Record class (i.e. substitute register).
    """
    def __init__(self, database):
        self.categories = Categories(database)
        self.categories.instanciate()
        self.products = Products(self.categories)
        self.products.instanciate()
        self.substitutes = Substitutes(self.products)
        self.substitutes.instanciate()
        self.compositions = Compositions(self.categories, self.products, self.substitutes, database)
        self.compositions.record_nominal_scenario()
