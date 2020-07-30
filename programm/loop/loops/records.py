#-*-coding:utf-8 -*
"""Records module.
"""
from os import system

from programm.model.record import Record

class Records:
    """Records class.
    """
    def __init__(self):
        self.engin = None
        self.menu = None
        self.categories = None
        self.products = None
        self.substitutes = None
        self.category = None
        self.product = None
        self.substitute = None
        self.records_list = []


    def watch(self, engin):
        """Method that starts records watch.
        """
        self.engin = engin
        self.menu = engin.menu
        self.show()

    def get_product(self, substitute):
        """Method that get the entire product information by joining
        substitute's product_product_id and product's id_product.
        """
        self.product = [product for product in\
        self.products.products_list if product.id_product ==\
        substitute.product_product_id]

    def get_substitute(self, substitute):
        """Method that get the entire substituted product informations
        by joining substitute's substitute_product_id and product's
        id_product.
        """
        self.substitute = [product for product in\
        self.products.products_list if product.id_product ==\
        substitute.substitute_product_id]

    def get_category(self, product):
        """Method that get the product category informations by joining
        product's category_id and category's id_category.
        """
        self.category = [category for category in\
        self.categories.categories_list if category.id_category ==\
        product[0].category_id]

    def set_records_list(self, engin):
        """Method that create the records' list.
        """
        self.records_list.clear()
        self.categories = engin.categories
        self.products = engin.products
        self.substitutes = engin.substitutes
        for substitute in self.substitutes.substitutes_registered_list:
            self.get_product(substitute)
            self.get_substitute(substitute)
            self.get_category(self.product)
            record = Record(self.category[0], self.product[0],\
            self.substitute[0])
            self.records_list.append(record)

    def show(self):
        """Method that propose/show the records to the user.
        """
        if self.records_list:
            print("Products & registered substitutes:")
            rank = 1
            for elt in self.records_list:
                print(rank, "."\
                "\n    Product name:", elt.product_product_name,\
                "(", elt.product_nutriscore_grade.capitalize(), ")",\
                "\n    Substitute name:", elt.substitute_product_name,\
                "(", elt.substitute_nutriscore_grade.capitalize(), ")")
                rank += 1
            system("pause")
            system("cls")
            self.menu.start(self.engin)
        else:
            print("No substitutes have been registered yet")
            system("pause")
            system("cls")
            self.menu.start(self.engin)
