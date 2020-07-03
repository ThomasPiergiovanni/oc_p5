#-*-coding:utf-8 -*
import urllib.request
import json
import operator

import config


class Products():
    def __init__(self):
        self.source_data = {}
        self.products_list = []

    def get_data(self,category_instance):
        url = config.PRODUCTS_ENDPOINT_BEGINNING + category_instance.id_origin + config.PRODUCTS_ENDPOINT_END +"?page_size=100" # elt.id_origin
        request = urllib.request.Request(url, headers = config.HEADER, method = 'GET')
        response = urllib.request.urlopen(request)
        self.source_data = response

        print(json.loads(response))

    def test(self):
        for elt in self.source_data["products"]:
            try:
                if elt["product_name"] and elt["id"]:
                    print (elt["id"], elt["product_name"] )
                else:
                    print("missing")
            except:
                pass

    def insert(self, category_instance, database_instance):
        statement = "INSERT INTO product (id_origin, product_name_origin,\
         url_origin, countries_origin, countries_tags_origin,\
         nutriscore_grade_origin, stores_origin, purchase_places_origin,\
         purchase_places_tags_origin, category_id, categories_tags_origin,\
         categories_origin ) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)"
        value = []
        for elt in self.source_data["products"]:
            if elt["id"] and elt["product_name"] and elt["nutriscore_grade"]:
                elt_string = (elt["id"], elt["product_name"], elt["url"], elt["countries"],\
                 elt["countries_tags"], elt["nutriscore_grade"], elt["stores"], elt["purchase_places"],\
                 elt["purchase_places_tags"], category_instance.id_category,\
                 elt["categories_tags"], elt["categories"])
                value.append(elt_string)
            else:
                pass
        database_instance.cursor.executemany(statement, value)
        database_instance.database.commit()

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
