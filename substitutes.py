#-*-coding:utf-8 -*

from database import Database
import substitute
import database
import research
import initialisation
import tests

class Substitutes:
    def __init__(self):
        self.database = Database()
        self.substitutes_proposed_list = []
        self.sorted_substitutes = []
        self.question = None
        self.select_input_valid = False
        self.selected_substitute = None
        self.register_input_valid = False
        self.registration = False
        self.substitutes_registered_list = []
        self.instanciate_substitute()

    def instanciate_substitute(self):
        self.database.cursor.execute ("SELECT * FROM p5.substitute")
        selection = self.database.cursor.fetchall()
        for elt in selection:
            product_product_id= elt[0]
            substitute_product_id = elt[1]
            substitute_instance = substitute.Substitute(product_product_id,\
            substitute_product_id)
            self.substitutes_registered_list.append(substitute_instance)    

    def process (self, products_instance):
        self.find(products_instance)
        self.organize()
        self.show()
        self.select()
        self.execute_selection()
        self.register()
        self.execute_registration()

    def find(self, products_instance):
        for elt in products_instance.selected_products:
            if elt.id_product != products_instance.selected_product.id_product and\
            elt.nutriscore_grade < products_instance.selected_product.nutriscore_grade:
                self.substitutes_proposed_list.append(elt)

    def organize(self):
        if self.substitutes_proposed_list:
            print ("SUBSTITUTES:")
            self.sorted_substitutes = sorted(self.substitutes_proposed_list, key = lambda \
            product : product.nutriscore_grade)
        else: 
            print("There is no healthier substitute for that product")
            initialisation.Initialisation.initiate()      

    def show(self):
        rank = 1
        for elt in self.sorted_substitutes:
            elt.temp_substitute_rank = rank
            print (elt.temp_substitute_rank ," - ",elt.product_name,\
            " - ", elt.nutriscore_grade)
            rank += 1

    def select(self):
        self.question= input("Which substitute you want to choose?\n")
        tests_instance = tests.Tests()
        tests.Tests.test_integer(tests_instance, self.question)
        if tests_instance.valid:
            self.select_input_valid = True

    def execute_selection(self):
        if self.select_input_valid:
            self.question = int(self.question)
            if self.question <= len(self.substitutes_proposed_list):
                for elt in self.substitutes_proposed_list:
                    if elt.temp_substitute_rank == self.question:
                        print ("You\'ve choosen the ", elt.product_name,\
                        "product as a substitute") 
                        self.selected_substitute = elt
            else:
                print ("Only numbers included in above list can be used. Retry")
                initialisation.Initialisation.initiate()
        else:
            print ("Only numbers can be used. Retry")
            initialisation.Initialisation.initiate()

    def register(self):
        self.question= input("Do you want to register that choice (y/n)?\n")
        tests_instance = tests.Tests()
        tests.Tests.test_string(tests_instance, self.question)
        if tests_instance.valid:
            self.register_input_valid = True

    def execute_registration(self):
        if self.register_input_valid:
            self.question = str(self.question)
            if self.question in "yY":
                self.registration = True
                print("Substitute product has been registered !") 
            elif self.question in "nN":
                initialisation.Initialisation.initiate()
        else:
            print ("Only letter y/n can be used. Retry ")
            initialisation.Initialisation.initiate()



