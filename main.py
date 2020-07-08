#-*-coding:utf-8 -*

import database
import download
import categories
import products
import reinitialisation



def client_category(categories_instance):
    categories.Categories.show(categories_instance)
    categories.Categories.select(categories_instance)

def client_product(database_instance, products_instance, categories_instance):
    products.Products.show(products_instance, categories_instance)
    products.Products.select(products_instance, categories_instance)
    products.Products.filter_substitutes(products_instance)
    products.Products.show_substitutes(products_instance)
    products.Products.select_substitute(products_instance)
    products.Products.register_substitute(products_instance, database_instance)

def main():
    reinitialisation.Reinitialisation.reinitialize()

    # products.Products.instanciate_product(products_instance, database_instance)
    # client_category(categories_instance)
    # client_product(database_instance, products_instance, categories_instance)

main()



