#-*-coding:utf-8 -*
"""Compositions module.
"""
from os import system

from programm.content.composition import Composition

class Compositions:
    """Compositions class.
    """
    def __init__(self):
        system("cls")
        self.compositions_list = []


    def start_record(self, engin):
        """Method that starts the compositions record
        nominal scenario.
        """
        self.engin = engin
        self.menu = engin.menu
        self.show()

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

    def set_compositions_list(self, engin):
        """Method that create the compositions instances.
        """
        self.compositions_list.clear()
        self.categories = engin.categories
        self.products = engin.products
        self.substitutes = engin.substitutes
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
        system("cls")
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
            system("pause")    
            self.menu.start_menu(self.engin)
        else:
            print("No substitutes have been registered yet")
            system("pause")
            self.menu.start_menu(self.engin)
