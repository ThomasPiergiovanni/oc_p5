#-*-coding:utf-8 -*

from database import Database
from categories import Categories
from products import Products
from menu import Menu
from reset import Reset

class Initialisation:
    def __init__(self):
        self.database = Database()
        self.categories = Categories(self.database)
        self.products = Products(self.database)

        self.initiate()

    def initiate(self):
        self.database.verify(self.database.exists())
        if self.database.status:
            self.database.execute_one(self.database.use())
            self.database.verify(self.categories.exists())
            self.database.verify(self.products.exists())
            # true n est pas correct
            if self.database.status:
                Menu(self.database)
            else:
                Reset(self.database)
        else:
            Reset(self.database)