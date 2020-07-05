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

    def insert(self, database_instance, category):
        statement = "INSERT INTO product (id_origin, product_name_origin,\
        nutriscore_grade_origin, category_id, categories_origin, countries_origin,\
        stores_origin) VALUES (%s, %s,%s, %s, %s,%s, %s)"
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
            except:
                pass
        database_instance.cursor.executemany(statement, value)
        database_instance.database.commit()

    def instanciate_product(self, database_instance):
        database_instance.cursor.execute ("SELECT * FROM product")
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




