#-*-coding:utf-8 -*

import categories
import products
import substitutes
import recompositions

class Registration:
    def registration(database_instance):
        categories_instance = categories.Categories()
        categories.Categories.instanciate_category(categories_instance, database_instance)

        products_instance = products.Products()
        products.Products.instanciate_product(products_instance, database_instance)

        substitutes_instance = substitutes.Substitutes()
        substitutes.Substitutes.instanciate_substitute(substitutes_instance, database_instance)

        recompositions_instance = recompositions.Recompositions()
        recompositions.Recompositions.instanciate_recomposition(recompositions_instance,\
        substitutes_instance, categories_instance, products_instance)
        
        recompositions.Recompositions.show(recompositions_instance)