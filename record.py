#-*-coding:utf-8 -*

from database import Database
from categories import Categories
from products import Products
from substitutes import Substitutes

import products
import substitutes
import compositions

class Record:
    def __init__(self):
        self.database = Database()
        self.categories = Categories()
        self.products = Products()
        self.substitutes = Substitutes()
        self.get()

    def get(self):

        compositions_instance = compositions.Compositions()
        compositions.Compositions.instanciate_composition(compositions_instance,\
        self.substitutes, self.categories, self.products)
        
        compositions.Compositions.show(compositions_instance)