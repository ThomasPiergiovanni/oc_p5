#-*-coding:utf-8 -*
from categories import Categories
from products import Products
from substitutes import Substitutes
import initialisation

class Research:

    def __init__(self):
        self.categories = Categories()
        self.products = Products(self.categories)
        self.substitutes = Substitutes(self.products)
        initialisation.Initialisation.initiate()
     
