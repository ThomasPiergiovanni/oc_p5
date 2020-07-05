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
            response_api =requests.get(config.PRODUCTS_ENDPOINT, headers = config.HEADER, params = params  )
            self.source_data = response_api.json()
        except HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
        except Exception as other_error:
            print(f"Other error occurred: {other_error}")
        else:
            print(f"HTTP call to API for {category.id_origin} successfull")

    # def instanciate_product(self, elt, id_generator, category): 
    #     id_product = id_generator
    #     id_origin = elt["id"]
    #     product_name_origin = elt["product_name"]
    #     url_origin = elt["url"]
    #     countries_origin = elt["countries"]
    #     countries_tag_origin = elt["countries_tag"]
    #     nutriscore_grade_origin = elt["nutriscore_grade"]
    #     stores_origin = elt["stores"]
    #     purchase_places_origin = elt["purchase_places"]
    #     purchase_places_tags_origin = elt["purchase_places_tags"]
    #     category_id = category.id_category
    #     categories_tags_origin = elt["categories_tags"]
    #     categories_origin = elt["categories"]
    #     product_instance = product.Product(id_product, id_origin, product_name_origin,\
    #     url_origin,\
    #     countries_origin, countries_tag_origin, nutriscore_grade_origin,\
    #     stores_origin, purchase_places_origin, purchase_places_tags_origin,\
    #     category_id, categories_tags_origin, categories_origin)
    #     self.products_list.append(product_instance)           

    def keep_valid(self, category):
        id_incrementer = 1
        for elt in self.source_data["products"]:
            try:
                if elt["id"] and elt["product_name"] and elt["nutriscore_grade"]:
                    id_product = id_incrementer
                    id_origin = elt["id"]
                    product_name_origin = elt["product_name"]
                    nutriscore_grade_origin = elt["nutriscore_grade"]
                    category_id = category.id_category
                    product_instance = product.Product(id_product, id_origin, product_name_origin, nutriscore_grade_origin,category_id)
                    self.products_list.append(product_instance) 


                    # Products.instanciate_product(elt, id_incrementer, category)
                    print (product_instance.id_product, product_instance.id_origin, product_instance.product_name_origin,product_instance.category_id)
                    id_incrementer += 1

            except Exception as error:
                print(f" Error occurred: {error}")
                pass

        


    # def insert(self, database_instance):
    #     statement = "INSERT INTO product (id_origin, product_name_origin,\
    #     url_origin, countries_origin, countries_tags_origin,\
    #     nutriscore_grade_origin, stores_origin, purchase_places_origin,\
    #     purchase_places_tags_origin, category_id, categories_tags_origin,\
    #     categories_origin ) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)"
    #     value = []
    #     for elt in self.valid_products["products"]:
    #         elt_string = (elt["id"], elt["product_name"], elt["url"], elt["countries"],\
    #         elt["countries_tags"], elt["nutriscore_grade"], elt["stores"], elt["purchase_places"],\
    #         elt["purchase_places_tags"], category_instance.id_category,\
    #         elt["categories_tags"], elt["categories"])
    #         value.append(elt_string)
    #         database_instance.cursor.executemany(statement, value)
    #         database_instance.database.commit()

    # def initialize_product(self, category_instance):
    #     for elt in self.source_data["products"]:
    #         id = elt["id"]
    #         product_name = elt["product_name"]
    #         url = elt["url"]
    #         countries = elt["countries"]
    #         countries_tag = elt["countries_tag"]
    #         nutriscore_grade = elt["nutriscore_grade"]
    #         stores = elt["stores"]
    #         purchase_places = elt["purchase_places"]
    #         purchase_places_tags = elt["purchase_places_tags"]
    #         category_id = elt["category"]
    #         countries_tag = elt["countries_tag"]

