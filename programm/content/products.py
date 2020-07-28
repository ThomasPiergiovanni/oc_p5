#-*-coding:utf-8 -*
"""Products module.
"""
from os import system

from programm.admin import config
from programm.content.product import Product

class Products():
    """Products class.
    """
    def __init__(self):
        self.egin = None
        self.database = None
        self.tests = None
        self.substitutes = None
        self.selected_category = None
        self.source_data = {}
        self.products_list = []
        self.selected_products = []
        self.question = None
        self.selected_product = 0

    def initialization_nominal_scenario(self):
        """Method that starts the products initialization
        nominal scenario.
        """
        self.database.verify(self.exists())

    def reset_nominal_scenario(self):
        """Method that starts the products reset
        nominal scenario.
        """
        self.database.execute_one(self.create_table())
        for category in self.categories.categories_list:
            self.tests = Tests()
            self.database.download(self.source(category))
            self.database.execute_many(self.insert_in_table(category))

    def exists(self):
        """Method that provides the sql statement and
        message for products verification.
        """
        statement = "SELECT * FROM product"
        message = "No or empty product tables"
        parameters = [statement, message]
        return parameters

    def source(self, category):
        """Method that provides the appropriate settings
        for products download.
        """
        endpoint = config.PRODUCTS_ENDPOINT
        params = {
            "action":"process", "tagtype_0": "categories",
            "tag_contains_0":"contains", "tag_0":category.id_origin,
            "json":1, "page":1, "page_size": config.PRODUCTS_AMOUNT}
        parameters = [endpoint, params]
        return parameters

    def create_table(self):
        """Method that provides the sql statement for
        products creation.
        """
        statement = "CREATE TABLE IF NOT EXISTS product(\
            id_product SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,\
            id_origin VARCHAR(250) NOT NULL,\
            product_name VARCHAR(250) NOT NULL,\
            nutriscore_grade VARCHAR(250) NOT NULL,\
            category_id SMALLINT UNSIGNED NOT NULL,\
            url LONGTEXT NOT NULL,\
            stores VARCHAR(250),\
            PRIMARY KEY (id_product),\
            FOREIGN KEY (category_id) REFERENCES category(id_category),\
            CONSTRAINT unique_product_per_cat UNIQUE (id_origin, category_id)\
            )ENGINE=INNODB;"
        parameters = [statement, None]
        return parameters

    def insert_in_table(self, category):
        """Method that provides the sql statement for
        products insertion.
        """
        statement = "INSERT INTO product (id_origin, product_name,\
        nutriscore_grade, category_id, url, stores)\
        VALUES (%s, %s, %s, %s, %s, %s)"
        values = []
        self.tests.test_consistency(\
        self.categories.database.source["products"], category)
        self.tests.test_duplicate(self.tests.consistent_products)
        values = self.tests.unique_products
        parameters = [statement, values]
        return parameters

    def set_products_list(self, database):
        """Method that create the products instances.
        """
        database.open_cursor()
        database.cursor.execute("SELECT * FROM product")
        selection = database.cursor.fetchall()
        for elt in selection:
            product = Product(elt[0], elt[1], elt[2], elt[3], elt[4],\
            elt[5], elt[6])
            self.products_list.append(product)
        database.close_cursor()

    def research(self, engin):
        """Method that sorts, for dispaly purposes, the products
        by product name.
        """
        self.engin = engin
        self.tests = engin.tests
        self.substitutes = engin.substitutes
        self.selected_category = engin.categories.selected_category
        self.find()

    def find(self):
        self.selected_products.clear()
        for elt in self.products_list:
            if elt.category_id == self.selected_category.id_category:
                self.selected_products.append(elt)
        self.sort()

    def sort (self):
        self.selected_products = sorted(self.selected_products,\
        key=lambda product: product.product_name)
        self.show()

    def show(self):
        """Method that propose the products options to the user.
        """
        system("cls")
        print("You're looking for products in category \"",\
        self.selected_category.name, "\"")
        print("PRODUCTS (Nutriscore):")
        rank = 1
        for elt in self.selected_products:
            elt.temp_product_rank = rank
            print(elt.temp_product_rank, " - ", elt.product_name, "(",\
            elt.nutriscore_grade.capitalize(), ")")
            rank += 1
        self.ask()

    def ask(self):
        """Method that ask for products's option selection to the user.
        """
        self.question = input("Which product you want to find a \
substitute for?\n")
        self.select()

    def select(self):
        """Method that starts the selected product option.
        """
        system("cls")
        if self.tests.test_integer(self.question):
            self.question = int(self.question)
            if self.question <= len(self.selected_products):
                for elt in self.selected_products:
                    if elt.temp_product_rank == self.question:
                        self.selected_product = elt
                        self.substitutes.research(self.engin)
            else:
                print(config.MESSAGE_OOR)
                self.show()
        else:
            print(config.MESSAGE_OOR)
            self.show()
