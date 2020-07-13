#-*-coding:utf-8 -*

import recomposition

class Recompositions:
    def __init__(self):
        self.recompositions_list=[]

    def instanciate_recomposition(self,substitutes_instance, categories_instance, products_instance):
        for substitute in substitutes_instance.substitutes_registered_list:

            product  = [product for product in\
            products_instance.products_list if product.id_product ==\
            substitute.product_product_id]

            substitute = [product for product in\
            products_instance.products_list if product.id_product ==\
            substitute.substitute_product_id]

            category = [category for category in\
            categories_instance.categories_list if category.id_category ==\
            product[0].category_id]


            recomposition_instance = recomposition.Recomposition(\
            product[0], substitute[0], category [0])

            self.recompositions_list.append(recomposition_instance)

    def show (self):
        rank = 1
        for elt in self.recompositions_list:
            print(rank,"."\
            "\n    Product name:", elt.product_product_name,\
            "\n    Substitute name:", elt.substitute_product_name)
            rank += 1
