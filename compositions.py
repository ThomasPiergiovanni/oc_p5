#-*-coding:utf-8 -*
"""Compositions module.
"""
from os import system

import menu
from composition import Composition

class Compositions:
    """Compositions class.
    """
    def __init__(self, categories, products, substitutes, database):
        system("cls")
        self.database = database
        self.categories = categories
        self.products = products
        self.substitutes = substitutes
        self.compositions_list = []
        self.category = None
        self.product = None
        self.substitute = None
        self.menu = menu.Menu(database)

    def record_nominal_scenario(self):
        """Method that starts the compositions record
        nominal scenario.
        """
        self.instanciate()
        self.show()

    def record_scenario_end(self):
        """Method that starts the end of the compsition record
        scenario.
        """
        system("pause")
        self.menu.menu_nominal_scenario()

    def get_product(self, substitute):
        """Method that get the product based on the recorded product id
        scenario.
        """
        self.product = [product for product in\
        self.products.products_list if product.id_product ==\
        substitute.product_product_id]

    def get_substitute(self, substitute):
        """Method that get the substitute product based on the recorded
        product id scenario.
        """
        self.substitute = [product for product in\
        self.products.products_list if product.id_product ==\
        substitute.substitute_product_id]

    def get_category(self, product):
        """Method that get the category based on product category id.
        """
        self.category = [category for category in\
        self.categories.categories_list if category.id_category ==\
        product[0].category_id]

    def instanciate(self):
        """Method that create the compositions instances.
        """
        for substitute in self.substitutes.substitutes_registered_list:
            self.get_product(substitute)
            self.get_substitute(substitute)
            self.get_category(self.product)
            composition = Composition(self.category[0], self.product[0],\
            self.substitute[0])
            self.compositions_list.append(composition)

    def show(self):
        """Method that shows the composed elements to the user.
        """
        if self.compositions_list:
            print("Products & registered substitutes:")
            rank = 1
            for elt in self.compositions_list:
                print(rank, "."\
                "\n    Product name:", elt.product_product_name,\
                "(", elt.product_nutriscore_grade.capitalize(), ")",\
                "\n    Substitute name:", elt.substitute_product_name,\
                "(", elt.substitute_nutriscore_grade.capitalize(), ")")
                rank += 1
            self.record_scenario_end()
        else:
            system("cls")
            print("No substitutes have been registered yet")
            self.record_scenario_end()
