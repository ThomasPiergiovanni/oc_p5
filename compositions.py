#-*-coding:utf-8 -*

from composition import Composition
import initialisation

class Compositions:
    def __init__(self, categories, products, substitutes):
        self.compositions_list=[]
        self.category = None
        self.product = None
        self.substitute = None
        self.instanciate_composition(categories, products, substitutes)
        self.show()

    def get_product(self, substitute, products):
            self.product  = [product for product in\
            products.products_list if product.id_product ==\
            substitute.product_product_id]

    def get_substitute(self, substitute, products):
            self.substitute = [product for product in\
            products.products_list if product.id_product ==\
            substitute.substitute_product_id]

    def get_category(self, categories, product):
            self.category = [category for category in\
            categories.categories_list if category.id_category ==\
            product[0].category_id]

    def instanciate_composition(self, categories, products, substitutes):
        for substitute in substitutes.substitutes_registered_list:

            self.get_product(substitute, products)
            self.get_substitute(substitute, products)
            self.get_category(categories, self.product)
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
            initialisation.Initialisation.initiate()
        else:
            print("No substitutes have been registered yet")
            initialisation.Initialisation.initiate()




