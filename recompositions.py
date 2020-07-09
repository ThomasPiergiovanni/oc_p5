#-*-coding:utf-8 -*

import recomposition

class Recompositions:
    def __init__(self):
        self.recomposed
        self.recompositions_list=[]

    def recompose(self,substitutes_instance, categories_instance, products_instance):
        for substitute in substitutes_instance.substitutes_registered_list:
            recomposed_object = {}

            product  = [(product.id_product, product.product_name,\
            product.nutriscore_grade, product.url, product.stores, product.category_id)\
            for product in\
            products_instance.products_list if product.id_product ==\
            substitute.product_product_id]

            substitute = [(product.id_product, product.product_name,\
            product.nutriscore_grade, product.url, product.stores) for product in\
            products_instance.products_list if product.id_product ==\
            substitute.substitute_product_id]

            category = [category.name for category in\
            categories_instance.categories_list if category.id_category ==\
            product[0][5]]


            recomposition_instance = recomposition.Recomposition(\
            product[0][0],\
            product[0][1],\
            product[0][2],\
            product[0][3],\
            product[0][4],\
            product[0][5],\
            category[0],\
            substitute[0][0],\
            substitute[0][1],\
            substitute[0][2],\
            substitute[0][3],\
            substitute[0][4])

            self.recompositions_list.append(recomposition_instance)

        for elt in self.recompositions_list:
            print(elt.product_product_name, "-", elt.substitute_product_name, "-", elt.category_name)
