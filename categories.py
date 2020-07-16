#-*-coding:utf-8 -*

import mysql.connector

from database import Database

import config
import category
import products
import tests

import initialisation

class Categories:
    def __init__(self):
        self.database = Database()
        self.categories_list=[]
        self.sorted_categories= []
        self.question = None
        self.select_input_valid = False
        self.selected_category = None 

    def instanciate_category(self):
        self.database.cursor.execute ("SELECT * FROM p5.category")
        selection = self.database.cursor.fetchall()
        for elt in selection:
            id_category = elt[0]
            id_origin = elt[1]
            name = elt[2]
            url = elt[3]
            category_instance = category.Category(id_category, id_origin,\
            name, url)
            self.categories_list.append(category_instance)

    def process (self):
        Categories.show(self)
        Categories.select(self)
        Categories.execute(self)

    def show(self):
        print ("CATEGORIES:")
        self.sorted_categories = sorted(self.categories_list, key = lambda \
        category : category.name)
        rank = 1
        for elt in self.sorted_categories:
            elt.temp_rank = rank
            print (elt.temp_rank ," - ",elt.name)
            rank += 1 

    def select(self):
        self.question= input("Which category you want to check products for?\n")
        tests_instance = tests.Tests()
        tests.Tests.test_integer(tests_instance, self.question)
        if tests_instance.valid:
            self.select_input_valid = True

    def execute(self):
        if self.select_input_valid:
            self.question = int(self.question)
            if self.question <= len(self.categories_list):
                for elt in self.categories_list:
                    if elt.temp_rank == self.question:
                        print ("You\'ve choosen the ", elt.name, "category") 
                        self.selected_category = elt
            else:
                print ("Only numbers included in above list can be used. Retry")
                initialisation.Initialisation.initiate()
        else:
            print ("Only numbers can be used. Retry")
            initialisation.Initialisation.initiate()










