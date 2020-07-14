#-*-coding:utf-8 -*

import categories
import products
import substitutes
import compositions

class Record:
    def get(database_instance):
        categories_instance = categories.Categories()
        categories.Categories.instanciate_category(categories_instance, database_instance)

        products_instance = products.Products()
        products.Products.instanciate_product(products_instance, database_instance)

        substitutes_instance = substitutes.Substitutes()
        substitutes.Substitutes.instanciate_substitute(substitutes_instance, database_instance)

        compositions_instance = compositions.Compositions()
        compositions.Compositions.instanciate_composition(compositions_instance,\
        substitutes_instance, categories_instance, products_instance)
        
        compositions.Compositions.show(compositions_instance)