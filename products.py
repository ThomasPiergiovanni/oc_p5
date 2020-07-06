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

    def get_data(self, category):
        try:
            params = {
                "action":"process",
                "tagtype_0": "categories",
                "tag_contains_0":"contains",
                "tag_0":category.id_origin,
                "json":1,
                "page":1,
                "page_size": config.PRODUCTS_AMOUNT}
            response_api =requests.get(config.PRODUCTS_ENDPOINT,\
            headers = config.HEADER, params = params)
            self.source_data = response_api.json()
        except HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
        except Exception as other_error:
            print(f"Other error occurred: {other_error}")
        else:
            print(f"HTTP call to API for {category.id_origin} successfull")

    def insert(self, database_instance, category):
        statement = "INSERT INTO product (id_origin, product_name_origin,\
        nutriscore_grade_origin, category_id, categories_origin,\
        countries_origin,\ stores_origin) VALUES (%s, %s,%s, %s, %s,%s, %s)"
        value = []
        for elt in self.source_data["products"]:
            try: 
                if elt["id"] and elt["product_name"] and elt["nutriscore_grade"]:
                    elt_string = (\
                    elt["id"],\
                    elt["product_name"],\
                    elt["nutriscore_grade"],\
                    category.id_category,\
                    elt["categories"],\
                    elt["countries"],\
                    # countries_tags_origin = elt["countries_tags"]
                    elt["stores"])
                    value.append(elt_string)
            except Exception as error:
                print(f"The following error occurred: {error}")
                pass
        database_instance.cursor.executemany(statement, value)
        database_instance.database.commit()

    def instanciate_product(self, database_instance):
        database_instance.cursor.execute ("SELECT * FROM p5.product")
        selection = database_instance.cursor.fetchall()   
        for elt in selection:
            id_product = elt[0]
            id_origin = elt[1]
            product_name_origin = elt[2]
            nutriscore_grade_origin = elt[3]
            category_id = elt[4]
            categories_origin = elt[5]
            countries_origin = elt[6]
            stores_origin = elt[7]


            product_instance = product.Product(\
            id_product,\
            id_origin,\
            product_name_origin,\
            nutriscore_grade_origin,\
            category_id,\
            categories_origin,\
            countries_origin,\
            # countries_tags_origin,\
            stores_origin)
                    
            self.products_list.append(product_instance)


    def show(self, categories_instance):
        print ("PRODUCTS:")
        for elt in self.products_list:
            if elt.category_id == categories_instance.selected_category:
                self.selected_products.append(elt)
                sorted_products = sorted(self.selected_products, key = lambda \
                product : product.product_name_origin)
        
        rank = 1
        for elt in sorted_products:
            print (rank ," - ",elt.product_name_origin)
            product_with_rank=(elt.id_product, elt.product_name_origin, rank)
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
        selected_product_nutriscore = [elt.nutriscore_grade_origin for elt in\
        self.selected_products if elt.id_product == self.selected_product]
        selected_product_nutriscore = selected_product_nutriscore [0]
        for elt in self.selected_products:
            if elt.id_product != self.selected_product and\
            elt.nutriscore_grade_origin < selected_product_nutriscore:
                self.substitutes_list.append(elt)

    def show_substitutes(self):
        print ("SUBSTITUTES:")
        sorted_substitutes = sorted(self.substitutes_list, key = lambda \
        product : product.nutriscore_grade_origin)
        rank = 1
        for elt in sorted_substitutes:
            print (rank ," - ",elt.product_name_origin, " - ", elt.nutriscore_grade_origin)
            substitutes_with_rank=(elt.id_product,\
            elt.product_name_origin, elt.nutriscore_grade_origin, rank)
            self.substitutes_with_rank.append(substitutes_with_rank)
            rank += 1
        

