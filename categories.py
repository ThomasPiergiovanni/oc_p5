#-*-coding:utf-8 -*

import requests
import json
import operator
import mysql.connector

import config
import category
import products

class Categories:
    def __init__(self):
        self.source_data = {}
        self.categories_list=[]

    def get_data(self):
        response_api =requests.get(config.CATEGORIES_ENDPOINT, headers = config.HEADER )
        self.source_data = response_api.json()

    def insert(self, database_instance):
        statement = "INSERT INTO category (id_origin, name_origin,\
         url_origin, products_origin) VALUES (%s, %s, %s,%s)"
        value = []
        for elt in self.source_data["tags"]:
            if elt["id"] in config.SELECTED_CATEGORIES and elt["name"] and elt["url"] and elt["products"]:
                elt_string = (elt["id"], elt["name"], elt["url"], elt["products"])
                value.append(elt_string)
            else:
                pass
        database_instance.cursor.executemany(statement, value)
        database_instance.database.commit()

    def instanciate_category(self, database_instance):
        database_instance.cursor.execute ("SELECT * FROM category")
        selection = database_instance.cursor.fetchall()
        for elt in selection:
            id_category = elt[0]
            id_origin = elt[1]
            name_origin = elt[2]
            url_origin = elt[3]
            products_origin = elt[4]
            category_instance = category.Category(id_category, id_origin, name_origin, url_origin, products_origin)
            self.categories_list.append(category_instance)

            print (category_instance.id_category)













    # def initialize(self):
    #     for elt in self.source_data["tags"]:
    #         id = elt["id"]
    #         name = elt["name"]
    #         url = elt["url"]
    #         products = elt["products"]
    #         category_instance = category.Category(id, name, url, products)
    #         self.categories_list.append(category_instance)

    # def insert(self, database_instance):
    #     statement = "INSERT INTO category (id_origin, name_origin,\
    #      url_origin, products_origin) VALUES (%s, %s, %s,%s)"
    #     value = []
    #     for elt in self.categories_list:
    #         if elt.id and elt.name and elt.url and elt.products:
    #             elt_string = (elt.id, elt.name, elt.url, elt.products)
    #             value.append(elt_string)
    #         else:
    #             pass
    #     database_instance.cursor.executemany(statement, value)
    #     database_instance.database.commit()

    # def wanted(self):
    #     for elt in self.categories_list:
    #         if elt.id in config.SELECTED_CATEGORIES:
    #             self.wanted_categories.append(elt)
    #         else:
    #             pass



        # for elt in self.wanted_categories:
        #     print (elt.id)

