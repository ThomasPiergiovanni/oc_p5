#-*-coding:utf-8 -*

from database import Database
from categories import Categories
from products import Products
from substitutes import Substitutes
from compositions import Compositions


class Record:
    def __init__(self):
        self.database = Database()
        self.categories = Categories()
        self.products = Products()
        self.substitutes = Substitutes()
        self.compositions= Compositions(self.categories, self.products,\
        self.substitutes)
