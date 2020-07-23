#-*-coding:utf-8 -*

from os import system

from composition import Composition
import menu

class Compositions:
    def __init__(self, categories, products, substitutes, database):
        system("cls")
        self.database = database
        self.categories = categories
        self.compositions_list=[]
        self.category = None
        self.product = None
        self.substitute = None
        self.menu = menu.Menu(database)
        self.instanciate_composition(products, substitutes)
        self.show()

    def get_product(self, substitute, products):
            self.product  = [product for product in\
            products.products_list if product.id_product ==\
            substitute.product_product_id]

    def get_substitute(self, substitute, products):
            self.substitute = [product for product in\
            products.products_list if product.id_product ==\
            substitute.substitute_product_id]

    def get_category(self, product):
            self.category = [category for category in\
            self.categories.categories_list if category.id_category ==\
            product[0].category_id]

    def instanciate_composition(self,products, substitutes):
        for substitute in substitutes.substitutes_registered_list:

            self.get_product(substitute, products)
            self.get_substitute(substitute, products)
            self.get_category(self.product)
            composition = Composition(self.category[0], self.product[0],\
            self.substitute[0])
            self.compositions_list.append(composition)

    def show(self):
        if self.compositions_list:
            rank = 1
            for elt in self.compositions_list:
                print(rank,"."\
                "\n    Product name:", elt.product_product_name,\
                "\n    Substitute name:", elt.substitute_product_name)
                rank += 1
            system("pause")
            self.menu.menu_nominal_scenario()
        else:
            system("cls")
            print("No substitutes have been registered yet")
            self.menu.menu_nominal_scenario()




