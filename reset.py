#-*-coding:utf-8 

from database import Database
from download import Download
from categories import Categories
from products import Products
import menu

class Reset:
    def __init__(self):
        self.database = Database()
        self.download = Download()
        self.categories = None
        self.products = None
        self.reset()

    def reset(self):
        self.database.delete()
        self.database.create()
        self.download.categories()
        self.database.insert_categories(self.download)
        self.categories = Categories()
        for category in self.categories.categories_list:
            self.download.products(category)
            self.database.insert_products(self.download, category)
        self.products = Products()
        menu.Menu()

