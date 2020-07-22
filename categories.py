#-*-coding:utf-8 -*

from os import system
import mysql.connector

from category import Category
from tests import Tests
import config

class Categories:
    def __init__(self, database):
        # system("cls")
        self.database = database
        self.categories_list=[]
        self.sorted_categories= []
        self.question = None
        self.tests = Tests()
        self.select_input_valid = False
        self.selected_category = None

    def reset_nominal_scenario(self):
        self.database.download(self.source())
        self.database.execute_one(self.create_table())
        self.database.execute_many(self.insert_in_table())
        self.instanciate()

    def research_nominal_scenario(self):
        self.instanciate()
        self.show()
        self.ask()
        self.select()

    def research_exception_scenario(self):
        self.show()
        self.ask()
        self.select()

    def exists(self):
        statement = "SELECT * FROM category"
        message= "No or empty category tables"
        parameters = [statement, message]
        return parameters

    def source(self):
        endpoint = config.CATEGORIES_ENDPOINT
        params= {}
        parameters = [endpoint, params]
        return parameters

    def create_table(self):
        statement = "CREATE TABLE IF NOT EXISTS category(\
            id_category SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,\
            id_origin VARCHAR(250) NOT NULL,\
            name VARCHAR(250) NOT NULL,\
            url LONGTEXT NOT NULL,\
            PRIMARY KEY (id_category)\
            )ENGINE=INNODB;"
        parameters =[statement, None]
        return parameters

    def insert_in_table(self):
        statement = "INSERT INTO category (id_origin, name,\
        url) VALUES (%s, %s, %s)"
        values = []
        for elt in self.database.source["tags"]:
            if elt["id"] in config.SELECTED_CATEGORIES and elt["name"] and\
            elt["url"]:
                elt_string = (elt["id"], elt["name"], elt["url"])
                values.append(elt_string)
            else:
                pass
        parameters = [statement, values]
        return parameters

    def instanciate(self):
        self.database.open_cursor()
        self.database.cursor.execute ("SELECT * FROM category")
        selection = self.database.cursor.fetchall()
        for elt in selection:
            category = Category(elt[0], elt[1],\
            elt[2], elt[3])
            self.categories_list.append(category)
        self.database.close_cursor()

    def show(self):
        print ("CATEGORIES:")
        self.sorted_categories = sorted(self.categories_list, key = lambda \
        category : category.name)
        rank = 1
        for elt in self.sorted_categories:
            elt.temp_rank = rank
            print (elt.temp_rank ," - ",elt.name)
            rank += 1 

    def ask(self):
        self.question= input("Which category you want to check products for?\n")
        self.tests.test_integer(self.question)
        if self.tests.valid:
            self.select_input_valid = True

    def select(self):
        if self.select_input_valid:
            self.question = int(self.question)
            if self.question <= len(self.categories_list):
                for elt in self.categories_list:
                    if elt.temp_rank == self.question:
                        print ("You\'ve choosen the ", elt.name, "category") 
                        self.selected_category = elt
            else:
                system("cls")
                print ("Only numbers included in above list can be used. Retry")
                self.research_exception_scenario()
        else:
            system("cls")
            print ("Only numbers can be used. Retry")
            self.research_exception_scenario()










