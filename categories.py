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
        self.selected_category = 0 

    def insert(self, database_instance):
        statement = "INSERT INTO category (id_origin, name_origin,\
         url_origin) VALUES (%s, %s, %s)"
        value = []
        for elt in self.source_data["tags"]:
            if elt["id"] in config.SELECTED_CATEGORIES and elt["name"] and\
            elt["url"]:
                elt_string = (elt["id"], elt["name"], elt["url"])
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
            name = elt[2]
            url = elt[3]
            category_instance = category.Category(id_category, id_origin,\
            name, url)
            self.categories_list.append(category_instance)

    def show(self):
        print ("CATEGORIES:")
        sorted_categories = sorted(self.categories_list, key = lambda \
        category : category.name)
        rank = 1
        for elt in sorted_categories:
            print (rank ," - ",elt.name)
            category_with_rank=(elt.id_category, elt.name, rank)
            self.categories_with_rank.append(category_with_rank)
            rank += 1 

    def select(self):
        question= input("Which category you want to check products for ?")
        question = int(question)
        for elt in self.categories_with_rank:
            if elt[2] == question:
                print ("You\'ve choosen the ", elt[1], "category") 
                self.selected_category = elt[0]








