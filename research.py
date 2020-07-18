#-*-coding:utf-8 -*

from categories import Categories
from products import Products
from substitutes import Substitutes
import menu

class Research:
    def __init__(self):
        self.categories = Categories()
        self.categories.process()
        self.products = Products()
        self.products.process(self.categories)
        self.substitutes = Substitutes()
        self.substitutes.process(self.products)

     
