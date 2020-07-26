#-*-coding:utf-8 -*
"""Research module.
"""
from programm.content.categories import Categories
from programm.content.products import Products
from programm.content.substitutes import Substitutes

class Research:
    """Research class(i.e. Search, find and register a product
    substitute).
    """
    def __init__(self, database):
        self.database = database
        self.categories = Categories(self.database)
        self.categories.research_nominal_scenario()
        self.products = Products(self.categories)
        self.products.research_nominal_scenario()
        self.substitutes = Substitutes(self.products)
        self.substitutes.research_nominal_scenario()
