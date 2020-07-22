#-*-coding:utf-8 

from categories import Categories
from products import Products
from substitutes import Substitutes
import initialisation
import menu

class Reset:
    def __init__(self, database):
        self.database = database
        self.categories = Categories(self.database)
        self.products = Products(self.categories)
        self.substitutes = Substitutes (self.products)
        self.database.reset_nominal_scenario()
        self.categories.reset_nominal_scenario()
        self.products.reset_nominal_scenario()
        self.substitutes.reset_nominal_scenario()
        menu.Menu(self.database)
        


        

