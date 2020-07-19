#-*-coding:utf-8 -*

from os import system
import config

from database import Database
from categories import Categories
from product import Product
from tests import Tests


class Products():
    def __init__(self):
        # system("cls")
        self.database = Database()
        self.source_data = {}
        self.products_list = []
        self.selected_products = []
        self.sorted_products = []
        self.question = None
        self.tests = Tests()
        self.select_input_valid = False
        self.selected_product = 0
        self.instanciate_product()

    def instanciate_product(self):
        self.database.open_cursor()
        self.database.cursor.execute ("SELECT * FROM p5.product")
        selection = self.database.cursor.fetchall()   
        for elt in selection:
            id_product = elt[0]
            id_origin = elt[1]
            product_name = elt[2]
            nutriscore_grade = elt[3]
            category_id = elt[4]
            url = elt[5]
            stores = elt[6]
            product = Product(id_product, id_origin,\
            product_name, nutriscore_grade, category_id, url, stores)        
            self.products_list.append(product)
        self.database.close_cursor()

    def process (self, categories):
        self.organize(categories)
        self.show()
        self.select()
        self.execute(categories)

    def organize(self, categories):
        for elt in self.products_list:
            if elt.category_id == categories.selected_category.id_category:
                self.selected_products.append(elt)
                self.sorted_products = sorted(self.selected_products, key = lambda \
                product : product.product_name)

    def show(self):
        print ("PRODUCTS:")
        rank = 1
        for elt in self.sorted_products:
            elt.temp_product_rank = rank
            print (elt.temp_product_rank ," - ",elt.product_name)
            rank += 1 

    def select(self):
        self.question= input("Which product you want to find a substitute for?\n")
        self.tests.test_integer(self.question)
        if self.tests.valid:
            self.select_input_valid = True

    def execute(self, categories):
        if self.select_input_valid:
            self.question = int(self.question)
            if self.question <= len(self.selected_products):
                for elt in self.selected_products:
                    if elt.temp_product_rank == self.question:
                        print ("You\'ve choosen the \"", elt.product_name, "\" product") 
                        self.selected_product = elt
            else:
                system("cls")
                print ("Only numbers included in above list can be used. Retry")
                self.show()
                self.select()
                self.execute(categories)
        else:
            system("cls")
            print ("Only numbers can be used. Retry")
            self.show()
            self.select()
            self.execute(categories)



       