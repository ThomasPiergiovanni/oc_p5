#-*-coding:utf-8 -*

from categories import Categories
from products import Products
from substitutes import Substitutes
import menu

class Research:
    def __init__(self, database):
        self.categories = Categories(database)
        self.categories.process()
        self.products = Products(database)
        self.products.process(self.categories)
        self.substitutes = Substitutes(database)
        self.substitutes.process(self.products)

     
