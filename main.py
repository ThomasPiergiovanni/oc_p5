#-*-coding:utf-8 -*

import database
import categories
import products


def initiate_db():
    database_instance = database.Database()
    return database_instance

def create_db(database_instance):   
    database.Database.create(database_instance)

def create_category(database_instance):

    categories_instance = categories.Categories()
    # categories.Categories.get_data(categories_instance)
    # categories.Categories.insert(categories_instance, database_instance)
    categories.Categories.instanciate_category(categories_instance, database_instance)
    return categories_instance

def create_product(database_instance, categories_instance):
    products_instance = products.Products()
    # for category in categories_instance.categories_list:
        # products.Products.get_data(products_instance, category)
        # products.Products.insert(products_instance, database_instance, category)
    products.Products.instanciate_product(products_instance, database_instance)
    return products_instance

def client_category(categories_instance):
    categories.Categories.show(categories_instance)
    categories.Categories.select(categories_instance)

def client_product(products_instance, categories_instance):
    products.Products.show(products_instance, categories_instance)
    products.Products.select(products_instance, categories_instance)
    products.Products.filter_substitutes(products_instance)
    products.Products.show_substitutes(products_instance)
    products.Products.select_substitute(products_instance)

def main():

    database_instance = initiate_db()
    # create_db(database_instance)
    categories_instance = create_category(database_instance)
    products_instance = create_product(database_instance, categories_instance)
    client_category(categories_instance)
    client_product(products_instance, categories_instance)

main()



