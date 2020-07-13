#-*-coding:utf-8 -*

import config
import product


class Products():
    def __init__(self):
        self.source_data = {}
        self.products_list = []
        self.selected_products = []
        self.products_with_rank =[]
        self.selected_product = 0

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
            product_instance = product.Product(id_product, id_origin,\
            product_name, nutriscore_grade, category_id, url, stores)        
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
        question= input("Which product you want to find a substitute for?\n")
        question = int(question)
        if question <= len(self.products_with_rank):
            for elt in self.products_with_rank:
                if elt[2] == question:
                    print ("You\'ve choosen the \"", elt[1], "\" product") 
                    self.selected_product = elt[0]
        else:
            print ("Only numbers included in above list can be used. Retry ")
            Products.select(self, categories_instance)

       