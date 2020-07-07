#-*-coding:utf-8 -*

import database
import download
import categories
import products




def create_product(database_instance, categories_instance):
    products_instance = products.Products()

    products.Products.instanciate_product(products_instance, database_instance)
    return products_instance

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

    database_instance = database.Database()
    # database.Database.create(database_instance)
    download_instance = download.Download()
    # download.Download.categories(download_instance)
    # database.Database.insert_categories(database_instance, download_instance)

    categories_instance = categories.Categories()
    categories.Categories.instanciate_category(categories_instance, database_instance)

    # for category in categories_instance.categories_list:
    #     download.Download.products(download_instance, category)
    #     database.Database.insert_products(database_instance, download_instance,category)
    products_instance = products.Products()
    products.Products.instanciate_product(products_instance, database_instance)
    # client_category(categories_instance)
    # client_product(database_instance, products_instance, categories_instance)

main()



