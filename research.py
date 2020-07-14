#-*-coding:utf-8 -*
import categories
import products
import substitutes
import database
import initialisation

class Research:

    def research(menu_instance, database_instance):
        categories_instance = categories.Categories()
        categories.Categories.instanciate_category(categories_instance,\
        database_instance)

        products_instance = products.Products()
        products.Products.instanciate_product(products_instance, database_instance)

        substitutes_instance = substitutes.Substitutes()

        categories.Categories.show(categories_instance)
        categories.Categories.select(categories_instance)

        products.Products.show(products_instance, categories_instance)
        products.Products.select(products_instance, categories_instance)

        substitutes.Substitutes.filter(substitutes_instance, products_instance)
        substitutes.Substitutes.show(substitutes_instance, menu_instance)
        substitutes.Substitutes.select(substitutes_instance)
        substitutes.Substitutes.register(substitutes_instance, menu_instance)
        database.Database.insert_substitute(database_instance,\
        products_instance, substitutes_instance)

        initialisation.Initialisation.initiate()

