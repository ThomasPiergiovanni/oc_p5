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
        self.categories_with_rank=[]

    def get_data(self):
        try:
            response_api =requests.get(config.CATEGORIES_ENDPOINT, headers = config.HEADER )
            self.source_data = response_api.json()
        except HTTPError as http_error:
            print(f'HTTP error occurred: {http_error}')
        except Exception as other_error:
            print(f'Other error occurred: {other_error}')  # Python 3.6
        else:
            print('HTTP call to API for categories successfull')

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
        database_instance.cursor.execute ("SELECT * FROM p5.category")
        selection = database_instance.cursor.fetchall()
        for elt in selection:
            id_category = elt[0]
            id_origin = elt[1]
            name_origin = elt[2]
            url_origin = elt[3]
            products_origin = elt[4]
            category_instance = category.Category(id_category, id_origin, name_origin, url_origin, products_origin)
            self.categories_list.append(category_instance)


    def show(self):

        sorted_categories = sorted(self.categories_list, key = lambda Category:Category.name_origin)
        rank = 1
        for elt in sorted_categories:
            print (rank ," - ",elt.name_origin)
            rank += 1 
            category_with_rank=(elt.id_category, elt.name_origin, rank)
            self.categories_with_rank.append(category_with_rank)



        # self.cursor.execute ("SELECT name_origin, id_category FROM p5.category ORDER BY name_origin ASC")
        # selection = self.cursor.fetchall()
        # question = "Select a category:"
        # print (question)
        # rank = 1
        # for elt in selection:
        #     name_origin = elt[0]
        #     print (rank," - ", name_origin)
        #     rank += 1 
        #     ordered_category=(id_category, name_origin, rank)
        #     self.ordered_categories.append(ordered_category)



