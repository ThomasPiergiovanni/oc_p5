#-*-coding:utf-8 -*
"""Substitutes module.
"""
from os import system

from programm.admin import config
from programm.structure import menu
from programm.content.substitute import Substitute
from programm.admin.tests import Tests

class Substitutes:
    """Substitutes class.
    """
    def __init__(self, products):
        system("cls")
        self.database = products.database
        self.menu = menu.Menu(self.database)
        self.products = products
        self.substitutes_proposed_list = []
        self.sorted_substitutes = []
        self.question = None
        self.tests = Tests()
        self.selected_substitute = None
        self.registration = False
        self.substitutes_registered_list = []

    def reset_nominal_scenario(self):
        """Method that starts the substitutes initialization
        nominal scenario.
        """
        self.database.execute_one(self.create_table())

    def research_nominal_scenario(self):
        """Method that starts the substitutes research
        nominal scenario.
        """
        self.instanciate()
        self.find()
        self.organize()
        self.show()
        self.ask()
        self.select()
        self.ask_registration()
        self.select_registration()
        self.database.execute_one(self.insert_in_table())
        self.research_scenario_end()

    def research_exception_scenario_one(self):
        """Method that starts the substitutes research
        1st exception scenario.
        """
        self.show()
        self.ask()
        self.select()
        self.ask_registration()
        self.select_registration()
        self.database.execute_one(self.insert_in_table())
        self.research_scenario_end()

    def research_exception_scenario_two(self):
        """Method that starts the substitutes research
        2nd exception scenario.
        """
        self.ask_registration()
        self.select_registration()
        self.database.execute_one(self.insert_in_table())
        self.research_scenario_end()

    def research_scenario_end(self):
        """Method that starts the end of the substitutes research
        scenario.
        """
        system("pause")
        system("cls")
        self.menu.menu_nominal_scenario()

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

    def instanciate(self):
        """Method that create the substitutes instances.
        """
        self.database.open_cursor()
        self.database.cursor.execute("SELECT * FROM substitute")
        selection = self.database.cursor.fetchall()
        for elt in selection:
            substitute = Substitute(elt[0], elt[1])
            self.substitutes_registered_list.append(substitute)
        self.database.close_cursor()

    def find(self):
        """Method that find a substitute to the product.
        """
        for elt in self.products.selected_products:
            if elt.id_product != self.products.selected_product.id_product and\
            elt.nutriscore_grade <\
            self.products.selected_product.nutriscore_grade:
                self.substitutes_proposed_list.append(elt)

    def organize(self):
        """Method that sorts, for dispaly purposes, the substitutes
        by product nutriscore grade.
        """
        if self.substitutes_proposed_list:
            self.sorted_substitutes = sorted(self.substitutes_proposed_list,\
            key=lambda product: product.nutriscore_grade)
        else:
            system("cls")
            print("There is no healthier substitute for that product")
            self.research_scenario_end()

    def show(self):
        """Method that propose the substitutes options to the user.
        """
        print("You're looking for substitute for product \"",\
        self.products.selected_product.product_name, "(",\
        self.products.selected_product.nutriscore_grade.capitalize(), ")", "\"")
        print("SUBSTITUTES (Nutriscore):")
        rank = 1
        for elt in self.sorted_substitutes:
            elt.temp_substitute_rank = rank
            print(elt.temp_substitute_rank, " - ", elt.product_name, "(",\
            elt.nutriscore_grade.capitalize(), ")")
            rank += 1

    def ask(self):
        """Method that ask for substitute's option selection to the user.
        """
        self.question = input("Which substitute you want to choose?\n")
        self.tests.test_integer(self.question)

    def select(self):
        """Method that starts the selected substitute option.
        """
        if self.tests.valid:
            system("cls")
            self.question = int(self.question)
            if self.question <= len(self.substitutes_proposed_list):
                for elt in self.substitutes_proposed_list:
                    if elt.temp_substitute_rank == self.question:
                        print("You\'ve choosen the following substitute:",\
                        "\n   - Product name:", elt.product_name,\
                        "\n   - Nutriscore value:",\
                        elt.nutriscore_grade.capitalize(),\
                        "\n   - Check product at:", elt.url,\
                        "\n   - Sold in:", elt.stores)
                        self.selected_substitute = elt
            else:
                print(config.MESSAGE_OOR)
                self.research_exception_scenario_one()
        else:
            system("cls")
            print(config.MESSAGE_OOR)
            self.research_exception_scenario_one()

    def ask_registration(self):
        """Method that ask for substitute registartion's option selection to the user.
        """
        self.question = input("Do you want to register that choice(y/n)?\n")
        self.tests.test_string(self.question)

    def select_registration(self):
        """Method that starts the selected registration option.
        """
        if self.tests.valid:
            system("cls")
            self.question = str(self.question)
            if self.question in "yY":
                self.registration = True
                print("Substitute product has been registered!")
            elif self.question in "nN":
                print("Substitute product hasn't been registered")
                self.research_scenario_end()
            else:
                system("cls")
                print(config.MESSAGE_YN)
                self.research_exception_scenario_two()
        else:
            system("cls")
            print(config.MESSAGE_YN)
            self.research_exception_scenario_two()

    def insert_in_table(self):
        """Method that provides the sql statement for
        substitute insertion.
        """
        if self.registration:
            statement = "INSERT INTO substitute (product_product_id,\
            substitute_product_id) VALUES (%s, %s)"
            values = [self.products.selected_product.id_product,\
            self.selected_substitute.id_product]
            parameters = [statement, values]
        return parameters
