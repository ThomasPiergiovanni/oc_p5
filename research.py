#-*-coding:utf-8 -*
import categories
import products
import substitutes
import database
import initialisation

class Research:

    def __init__(self):
        self.categories_instance = None
        self.products_instance = None
        self.substitutes_instance = None

    def instanciate(self, database_instance):
        self.categories_instance = categories.Categories()
        categories.Categories.instanciate_category(self.categories_instance,\
        database_instance)
        self.products_instance = products.Products()
        products.Products.instanciate_product(self.products_instance,\
        database_instance)
        self.substitutes_instance = substitutes.Substitutes()

    def research(self, database_instance, tests_instance):

        categories.Categories.process(self.categories_instance,\
        tests_instance)

        products.Products.process(self.products_instance,\
        self.categories_instance, tests_instance)

        substitutes.Substitutes.filter(self.substitutes_instance,\
        self.products_instance)
        substitutes.Substitutes.show(self.substitutes_instance)
        substitutes.Substitutes.select(self.substitutes_instance)
        substitutes.Substitutes.register(self.substitutes_instance)
        database.Database.insert_substitute(database_instance,\
        self.products_instance, self.substitutes_instance)

        initialisation.Initialisation.initiate()

