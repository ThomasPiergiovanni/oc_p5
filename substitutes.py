#-*-coding:utf-8 -*

from database import Database
from substitute import Substitute
from tests import Tests
import initialisation

class Substitutes:
    def __init__(self):
        self.database = Database()
        self.substitutes_proposed_list = []
        self.sorted_substitutes = []
        self.question = None
        self.tests = Tests()
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
            substitute = Substitute(product_product_id,\
            substitute_product_id)
            self.substitutes_registered_list.append(substitute)    

    def process (self, products):
        self.find(products)
        self.organize()
        self.show()
        self.select()
        self.execute_selection(products)
        self.register()
        self.execute_registration()
        self.insert_substitute(products)

    def find(self, products):
        for elt in products.selected_products:
            if elt.id_product != products.selected_product.id_product and\
            elt.nutriscore_grade < products.selected_product.nutriscore_grade:
                self.substitutes_proposed_list.append(elt)

    def organize(self):
        if self.substitutes_proposed_list:
            self.sorted_substitutes = sorted(self.substitutes_proposed_list,\
            key = lambda product : product.nutriscore_grade)
        else: 
            print("There is no healthier substitute for that product")
            initialisation.Initialisation()     

    def show(self):
        print ("SUBSTITUTES:")
        rank = 1
        for elt in self.sorted_substitutes:
            elt.temp_substitute_rank = rank
            print (elt.temp_substitute_rank ," - ",elt.product_name,\
            " - ", elt.nutriscore_grade)
            rank += 1

    def select(self):
        self.question= input("Which substitute you want to choose?\n")
        self.tests.test_integer(self.question)
        if self.tests.valid:
            self.select_input_valid = True

    def execute_selection(self, products):
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
                self.show()
                self.select()
                self.execute_selection(products)
                self.register()
                self.execute_registration()
                self.insert_substitute(products)
        else:
            print ("Only numbers can be used. Retry")
            self.show()
            self.select()
            self.execute_selection(products)
            self.register()
            self.execute_registration()
            self.insert_substitute(products)

    def register(self):
        self.question= input("Do you want to register that choice (y/n)?\n")
        self.tests.test_string(self.question)
        if self.tests.valid:
            self.register_input_valid = True

    def execute_registration(self):
        if self.register_input_valid:
            self.question = str(self.question)
            if self.question in "yY":
                self.registration = True
                print("Substitute product has been registered !") 
            elif self.question in "nN":
                initialisation.Initialisation()
            else : 
                print ("Only letter y/n can be used. Retry ")
                self.register()
                self.execute_registration()
                self.insert_substitute(products)
        else:
            print ("Only letter y/n can be used. Retry ")
            self.register()
            self.execute_registration()
            self.insert_substitute(products)

    def insert_substitute(self, products):
        if self.registration:
            statement = "INSERT INTO p5.substitute (product_product_id,\
            substitute_product_id) VALUES (%s, %s)"
            value = [products.selected_product.id_product,\
            self.selected_substitute.id_product]
            self.database.cursor.execute(statement, value)
            self.database.connection.commit()





