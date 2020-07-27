#-*-coding:utf-8 -*
"""Compositions module.
"""
from os import system

from programm.structure import menu
from programm.content.composition import Composition

class Compositions:
    """Compositions class.
    """
    def __init__(self):
        system("cls")
        self.compositions_list = []


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
        system("cls")
        self.menu.menu_nominal_scenario()

    def get_product(self, products, substitute):
        """Method that get the product based on the recorded product id
        scenario.
        """
        self.product = [product for product in\
        products.products_list if product.id_product ==\
        substitute.product_product_id]

    def get_substitute(self, products, substitute):
        """Method that get the substitute product based on the recorded
        product id scenario.
        """
        self.substitute = [product for product in\
        products.products_list if product.id_product ==\
        substitute.substitute_product_id]

    def get_category(self, categories, product):
        """Method that get the category based on product category id.
        """
        self.category = [category for category in\
        categories.categories_list if category.id_category ==\
        product[0].category_id]

    def instanciate(self, categories, products, substitutes):
        """Method that create the compositions instances.
        """
        for substitute in substitutes.substitutes_registered_list:
            self.get_product(products, substitute)
            self.get_substitute(products, substitute)
            self.get_category(categories, self.product)
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
