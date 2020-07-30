#-*-coding:utf-8 -*
"""Substitutes module.
"""
from os import system

from programm.admin import config
from programm.model.substitute import Substitute

class Substitutes:
    """Substitutes class.
    """
    def __init__(self):
        system("cls")
        self.engin = None
        self.database = None
        self.tests = None
        self.menu = None
        self.selected_products = None
        self.selected_product = None
        self.selected_substitutes = []
        self.question = None
        self.selected_substitute = None
        self.registration = False
        self.substitutes_registered_list = []

    def reset(self, engin):
        self.engin = engin
        self.database = engin.database 
        self.menu = engin.menu
        self.database.execute_one(self.create_table())
        self.engin.set_datas()
        self.menu.start(self.engin)

    def create_table(self):
        """Method that provides the sql statement for
        substitutes creation.
        """
        statement = "CREATE TABLE IF NOT EXISTS substitute(\
            product_product_id SMALLINT UNSIGNED NOT NULL,\
            substitute_product_id SMALLINT UNSIGNED NOT NULL,\
            FOREIGN KEY (product_product_id) REFERENCES product(id_product),\
            FOREIGN KEY (substitute_product_id) REFERENCES product(id_product)\
            )ENGINE=INNODB;"
        parameters = [statement, None]
        return parameters

    def set_substitutes_list(self, database):
        """Method that create the substitutes instances.
        """
        self.substitutes_registered_list.clear()
        database.open_cursor()
        database.cursor.execute("SELECT * FROM substitute")
        selection = database.cursor.fetchall()
        for elt in selection:
            substitute = Substitute(elt[0], elt[1])
            self.substitutes_registered_list.append(substitute)
        database.close_cursor()

    def research(self, engin):
        """Method that starts the substitutes research
        nominal scenario.
        """
        self.engin = engin
        self.database = engin.database
        self.tests = engin.tests
        self.menu = engin.menu
        self.selected_products = engin.products.selected_products
        self.selected_product = engin.products.selected_product
        self.find()

    def find(self):
        """Method that find a substitute to the product.
        """
        self.selected_substitutes.clear()
        for elt in self.selected_products:
            if elt.id_product != self.selected_product.id_product and\
            elt.nutriscore_grade < self.selected_product.nutriscore_grade:
                self.selected_substitutes.append(elt)
        self.sort()

    def sort(self):
        """Method that sorts, for dispaly purposes, the substitutes
        by product nutriscore grade.
        """
        if self.selected_substitutes:
            self.selected_substitutes = sorted(self.selected_substitutes,\
            key=lambda product: product.nutriscore_grade)
            self.show()
        else:
            system("cls")
            print("There is no healthier substitute for that product")
            system("pause")
            self.menu.start(self.engin)


    def show(self):
        """Method that propose the substitutes options to the user.
        """
        system("cls")
        print("You're looking for substitute for product \"",\
        self.selected_product.product_name, "(",\
        self.selected_product.nutriscore_grade.capitalize(), ")", "\"")
        print("SUBSTITUTES (Nutriscore):")
        rank = 1
        for elt in self.selected_substitutes:
            elt.temp_substitute_rank = rank
            print(elt.temp_substitute_rank, " - ", elt.product_name, "(",\
            elt.nutriscore_grade.capitalize(), ")")
            rank += 1
        self.ask()

    def ask(self):
        """Method that ask for substitute's option selection to the user.
        """
        self.question = input("Which substitute you want to choose?\n")
        self.select()

    def select(self):
        """Method that starts the selected substitute option.
        """
        system("cls")
        if self.tests.test_integer(self.question):
            self.question = int(self.question)
            if self.question <= len(self.selected_substitutes):
                for elt in self.selected_substitutes:
                    if elt.temp_substitute_rank == self.question:
                        print("You\'ve choosen the following substitute:",\
                        "\n   - Product name:", elt.product_name,\
                        "\n   - Nutriscore value:",\
                        elt.nutriscore_grade.capitalize(),\
                        "\n   - Check product at:", elt.url,\
                        "\n   - Sold in:", elt.stores)
                        self.selected_substitute = elt
                        self.ask_registration()
            else:
                print(config.MESSAGE_OOR)
                self.show()
        else:
            print(config.MESSAGE_OOR)
            self.show()

    def ask_registration(self):
        """Method that ask for substitute registartion's option selection to the user.
        """
        self.question = input("Do you want to register that choice(y/n)?\n")
        self.select_registration()

    def select_registration(self):
        """Method that starts the selected registration option.
        """
        if self.tests.test_string(self.question):
            system("cls")
            self.question = str(self.question)
            if self.question in "yY":
                self.registration = True
                self.database.execute_one(self.insert_in_table())
                self.engin.set_datas()
                print("Substitute product has been registered!")
                system("pause")
                self.menu.start(self.engin)
            elif self.question in "nN":
                print("Substitute product hasn't been registered")
                system("pause")
                self.menu.start(self.engin)
            else:
                print(config.MESSAGE_YN)
                self.ask_registration()
        else:
            system("cls")
            print(config.MESSAGE_YN)
            self.ask_registration()

    def insert_in_table(self):
        """Method that provides the sql statement for
        substitute insertion.
        """
        if self.registration:
            statement = "INSERT INTO substitute (product_product_id,\
            substitute_product_id) VALUES (%s, %s)"
            values = [self.selected_product.id_product,\
            self.selected_substitute.id_product]
            parameters = [statement, values]
        return parameters
