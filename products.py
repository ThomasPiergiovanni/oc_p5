#-*-coding:utf-8 -*
import requests
import json
import operator

import config
import product


class Products():
    def __init__(self):
        self.source_data = {}
        self.products_list = []
        self.selected_products = []
        self.products_with_rank =[]
        self.selected_product = 0
        self.substitutes_list = []
        self.substitutes_with_rank = []
        self.selected_substitute = 0

    def instanciate_product(self, database_instance):
        database_instance.cursor.execute ("SELECT * FROM p5.product")
        selection = database_instance.cursor.fetchall()   
        for elt in selection:
            id_product = elt[0]
            id_origin = elt[1]
            product_name = elt[2]
            nutriscore_grade = elt[3]
            category_id = elt[4]
            url = elt[5]
            stores = elt[6]


            product_instance = product.Product(\
            id_product,\
            id_origin,\
            product_name,\
            nutriscore_grade,\
            category_id,\
            url,\
            stores)
                    
            self.products_list.append(product_instance)


    def show(self, categories_instance):
        print ("PRODUCTS:")
        for elt in self.products_list:
            if elt.category_id == categories_instance.selected_category:
                self.selected_products.append(elt)
                sorted_products = sorted(self.selected_products, key = lambda \
                product : product.product_name)
        
        rank = 1
        for elt in sorted_products:
            print (rank ," - ",elt.product_name)
            product_with_rank=(elt.id_product, elt.product_name, rank)
            self.products_with_rank.append(product_with_rank)
            rank += 1 

    def select(self, categories_instance):
        question= input("Which product you want to find a substitute for ?")
        question = int(question)
        for elt in self.products_with_rank:
            if elt[2] == question:
                print ("You\'ve choosen the \"", elt[1], "\" product") 
                self.selected_product = elt[0]

    def filter_substitutes(self):
        selected_product_nutriscore = [elt.nutriscore_grade for elt in\
        self.selected_products if elt.id_product == self.selected_product]
        selected_product_nutriscore = selected_product_nutriscore [0]
        for elt in self.selected_products:
            if elt.id_product != self.selected_product and\
            elt.nutriscore_grade < selected_product_nutriscore:
                self.substitutes_list.append(elt)

    def show_substitutes(self):
        print ("SUBSTITUTES:")
        sorted_substitutes = sorted(self.substitutes_list, key = lambda \
        product : product.nutriscore_grade)
        rank = 1
        for elt in sorted_substitutes:
            print (rank ," - ",elt.product_name, " - ", elt.nutriscore_grade)
            substitutes_with_rank=(elt.id_product,\
            elt.product_name, elt.nutriscore_grade, rank)
            self.substitutes_with_rank.append(substitutes_with_rank)
            rank += 1

    def select_substitute(self):
        question= input("Which substitute you want to choose ?")
        question = int(question)
        for elt in self.substitutes_with_rank:
            if elt[3] == question:
                print ("You\'ve choosen the ", elt[1], "product as a substitute") 
                self.selected_substitute = elt[0]

    def register_substitute(self, database_instance):
        statement = "INSERT INTO p5.registration (product_product_id,\
        substitut_product_id) VALUES (%s, %s)"
        value = [self.selected_product, self.selected_substitute]
        database_instance.cursor.execute(statement, value)
        database_instance.database.commit()        
        