#-*-coding:utf-8 -*
"""Products module.
"""
from os import system

import config
from product import Product
from tests import Tests

class Products():
    """Products class.
    """
    def __init__(self, categories):
        system("cls")
        self.database = categories.database
        self.categories = categories
        self.source_data = {}
        self.products_list = []
        self.selected_products = []
        self.sorted_products = []
        self.question = None
        self.tests = Tests()
        self.select_input_valid = False
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

    def research_nominal_scenario(self):
        """Method that starts the products research
        nominal scenario.
        """
        self.instanciate()
        self.organize()
        self.show()
        self.tests = Tests()
        self.ask()
        self.select()

    def research_exception_scenario(self):
        """Method that starts the products research
        exception scenario.
        """
        self.show()
        self.tests = Tests()
        self.ask()
        self.select()

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

    def instanciate(self):
        """Method that create the products instances.
        """
        self.database.open_cursor()
        self.database.cursor.execute("SELECT * FROM product")
        selection = self.database.cursor.fetchall()
        for elt in selection:
            product = Product(elt[0], elt[1], elt[2], elt[3], elt[4],\
            elt[5], elt[6])
            self.products_list.append(product)
        self.database.close_cursor()

    def organize(self):
        """Method that sorts, for dispaly purposes, the products
        by product name.
        """
        for elt in self.products_list:
            if elt.category_id == self.categories.selected_category.id_category:
                self.selected_products.append(elt)
                self.sorted_products = sorted(self.selected_products,\
                key=lambda product: product.product_name)

    def show(self):
        """Method that propose the products options to the user.
        """
        print("You're looking for products in category \"",\
        self.categories.selected_category.name, "\"")
        print("PRODUCTS (Nutriscore):")
        rank = 1
        for elt in self.sorted_products:
            elt.temp_product_rank = rank
            print(elt.temp_product_rank, " - ", elt.product_name, "(",\
            elt.nutriscore_grade.capitalize(), ")")
            rank += 1

    def ask(self):
        """Method that ask for products's option selection to the user.
        """
        self.question = input("Which product you want to find a \
substitute for?\n")
        self.tests.test_integer(self.question)
        if self.tests.valid:
            self.select_input_valid = True

    def select(self):
        """Method that starts the selected option.
        """
        if self.select_input_valid:
            self.question = int(self.question)
            if self.question <= len(self.selected_products):
                for elt in self.selected_products:
                    if elt.temp_product_rank == self.question:
                        print("You\'ve choosen the \"", elt.product_name,\
                        "\" product")
                        self.selected_product = elt
            else:
                system("cls")
                print("Only numbers included in above list can be used. Retry")
                self.research_exception_scenario()
        else:
            system("cls")
            print("Only numbers can be used. Retry")
            self.research_exception_scenario()
