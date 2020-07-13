#-*-coding:utf-8 -*

import operator
import mysql.connector

import config
import category
import products

class Categories:
    def __init__(self):
        self.categories_list=[]
        self.categories_with_rank=[]
        self.selected_category = 0 

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
        question= input("Which category you want to check products for?\n")
        try:
            question = int(question)
            if question <= len(self.categories_with_rank):
                for elt in self.categories_with_rank:
                    if elt[2] == question:
                        print ("You\'ve choosen the ", elt[1], "category") 
                        self.selected_category = elt[0]
            else:
                print ("Only numbers included in above list can be used. Retry ")
                Categories.select(self)
        except:
            print ("Only numbers can be used. Retry ")
            Categories.select(self)










