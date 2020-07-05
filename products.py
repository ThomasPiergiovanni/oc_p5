#-*-coding:utf-8 -*
import requests
import json
import operator

import config


class Products():
    def __init__(self):
        self.source_data = {}
        self.products_list = []

    def get_data(self,categories_instance):
        for elt in categories_instance.categories_list:
            try:
                params = {
                    "action":"process",
                    "tagtype_0": "categories",
                    "tag_contains_0":"contains",
                    "tag_0":elt.id_origin,
                    "json":1,
                    "page":1,
                    "page_size": config.PRODUCTS_AMOUNT}
                response_api =requests.get(config.PRODUCTS_ENDPOINT, headers = config.HEADER, params = params  )
                self.source_data = response_api.json()
                for product in self.source_data["products"]:
                    try:
                        if product["product_name"] and product["id"]:
                             print (product["id"], product["product_name"] )
                        else:
                             print("missing")
                    except:
                        pass


            except HTTPError as http_error:
                print(f"HTTP error occurred: {http_error}")
            except Exception as other_error:
                print(f"Other error occurred: {other_error}")  # Python 3.6
            else:
                print(f"HTTP call to API for {elt.id_origin} successfull")



    #def test(self):


    # def insert(self, category_instance, database_instance):
    #     statement = "INSERT INTO product (id_origin, product_name_origin,\
    #      url_origin, countries_origin, countries_tags_origin,\
    #      nutriscore_grade_origin, stores_origin, purchase_places_origin,\
    #      purchase_places_tags_origin, category_id, categories_tags_origin,\
    #      categories_origin ) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)"
    #     value = []
    #     for elt in self.source_data["products"]:
    #         if elt["id"] and elt["product_name"] and elt["nutriscore_grade"]:
    #             elt_string = (elt["id"], elt["product_name"], elt["url"], elt["countries"],\
    #              elt["countries_tags"], elt["nutriscore_grade"], elt["stores"], elt["purchase_places"],\
    #              elt["purchase_places_tags"], category_instance.id_category,\
    #              elt["categories_tags"], elt["categories"])
    #             value.append(elt_string)
    #         else:
    #             pass
    #     database_instance.cursor.executemany(statement, value)
    #     database_instance.database.commit()

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
    #         products = elt["products"]
    #         category_instance = category.Category(id, name, url, products)
    #         self.categories_list.append(category_instance)
