#-*-coding:utf-8
"""Reset module.
"""
from categories import Categories
from products import Products
from substitutes import Substitutes
import menu

class Reset:
    """Reset class.
    """
    def __init__(self, database):
        self.database = database
        self.database.reset_nominal_scenario()
        self.categories = Categories(self.database)
        self.categories.reset_nominal_scenario()
        self.products = Products(self.categories)
        self.products.reset_nominal_scenario()
        self.substitutes = Substitutes(self.products)
        self.substitutes.reset_nominal_scenario()
        self.menu = menu.Menu(self.database)
        self.menu.menu_nominal_scenario()
