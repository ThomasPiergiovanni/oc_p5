#-*-coding:utf-8 -*

import config

from database import Database
from category import Category
from tests import Tests



class Categories:
    def __init__(self):
        self.database = Database()
        self.categories_list=[]
        self.sorted_categories= []
        self.question = None
        self.tests = Tests()
        self.select_input_valid = False
        self.selected_category = None
        self.instanciate_category()

    def instanciate_category(self):
        self.database.cursor.execute ("SELECT * FROM p5.category")
        selection = self.database.cursor.fetchall()
        for elt in selection:
            id_category = elt[0]
            id_origin = elt[1]
            name = elt[2]
            url = elt[3]
            category = Category(id_category, id_origin,\
            name, url)
            self.categories_list.append(category)

    def process (self):
        self.show()
        self.select()
        self.execute()

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
        self.tests.test_integer(self.question)
        if self.tests.valid:
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
                self.process()
        else:
            print ("Only numbers can be used. Retry")
            #initialisation.Initialisation.initiate()
            self.process()










