#-*-coding:utf-8 -*

from composition import Composition
import initialisation

class Compositions:
    def __init__(self, categories, products, substitutes):
        self.compositions_list=[]
        self.instanciate_composition(categories, products, substitutes)
        self.show()

    def instanciate_composition(self, categories, products, substitutes):
        for substitute in substitutes.substitutes_registered_list:

            product  = [product for product in\
            products.products_list if product.id_product ==\
            substitute.product_product_id]

            substitute = [product for product in\
            products.products_list if product.id_product ==\
            substitute.substitute_product_id]

            category = [category for category in\
            categories.categories_list if category.id_category ==\
            product[0].category_id]

            composition = Composition(product[0], substitute[0], category [0])

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




