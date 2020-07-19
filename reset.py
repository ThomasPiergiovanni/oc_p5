#-*-coding:utf-8 

from database import Database
from download import Download
from categories import Categories
from products import Products
import menu

class Reset:
    def __init__(self):
        self.database = Database()
        print ("here22")
        self.download = Download()
        print ("here23")
        self.categories = None
        self.products = None
        self.reset()
        print ("here24")

    def reset(self):
        self.database.delete()
        print ("here1")
        self.database.create()
        print ("here2")
        self.download.categories()
        print ("here3")
        self.database.insert_categories(self.download)
        print ("here4")
        self.categories = Categories()
        print ("here5")
        for category in self.categories.categories_list:
            self.download.products(category)
            print ("here6")
            self.database.insert_products(category, self.download)
            print ("here7")
        self.products = Products()
        print ("here8")
        menu.Menu()

