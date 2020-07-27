#-*-coding:utf-8 -*
"""Categories module.
"""
from os import system

from programm.admin import config
# from programm.admin.tests import Tests
from programm.content.category import Category

class Categories:
    """Categories class.
    """
    def __init__(self):
        self.database = None
        self.tests = None
        self.products = None
        self.substitutes = None
        self.categories_list = []
        self.question = None
        self.selected_category = None

    def reset_nominal_scenario(self):
        """Method that starts the categories reset
        nominal scenario.
        """
        self.database.download(self.source())
        self.database.execute_one(self.create_table())
        self.database.execute_many(self.insert_in_table())
        self.instanciate()

    def exists(self):
        """Method that provides the sql statement and
        message for categories verification.
        """
        statement = "SELECT * FROM category"
        parameters = [statement, None]
        return parameters

    def source(self):
        """Method that provides the appropriate settings
        for categories download.
        """
        endpoint = config.CATEGORIES_ENDPOINT
        params = {}
        parameters = [endpoint, params]
        return parameters

    def create_table(self):
        """Method that provides the sql statement for
        categories creation.
        """
        statement = "CREATE TABLE IF NOT EXISTS category(\
            id_category SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,\
            id_origin VARCHAR(250) NOT NULL,\
            name VARCHAR(250) NOT NULL,\
            url LONGTEXT NOT NULL,\
            PRIMARY KEY (id_category)\
            )ENGINE=INNODB;"
        parameters = [statement, None]
        return parameters

    def insert_in_table(self):
        """Method that provides the sql statement for
        categories insertion.
        """
        statement = "INSERT INTO category(id_origin, name,\
        url) VALUES(%s, %s, %s)"
        values = []
        for elt in self.database.source["tags"]:
            if elt["id"] in config.SELECTED_CATEGORIES and elt["name"] and\
            elt["url"]:
                elt_string = (elt["id"], elt["name"], elt["url"])
                values.append(elt_string)
            else:
                pass
        parameters = [statement, values]
        return parameters

    def instanciate(self, database):
        """Method that create the categories instances.
        """
        database.open_cursor()
        database.cursor.execute("SELECT * FROM category")
        selection = database.cursor.fetchall()
        for elt in selection:
            category = Category(elt[0], elt[1],\
            elt[2], elt[3])
            self.categories_list.append(category)
        database.close_cursor()

    def research(self, database, tests, products, substitutes):
        self.database = database
        self.tests = tests
        self.products = products
        self.substitutes = substitutes
        self.sort()

    def sort(self):
        self.categories_list = sorted(self.categories_list, key=lambda \
        category: category.name)
        self.show()

    def show(self):
        """Method that propose the categories options to the user.
        """
        system("cls")
        print("CATEGORIES:")
        rank = 1
        for elt in self.categories_list:
            elt.temp_rank = rank
            print(elt.temp_rank, " - ", elt.name)
            rank += 1
        self.ask()

    def ask(self):
        """Method that ask for category's option selection to the user.
        """
        self.question = input("Which category you want to \
check products for?\n")
        self.select()

    def select(self):
        """Method that starts the selected category option.
        """
        system("cls")
        if self.tests.test_integer(self.question):
            self.question = int(self.question)
            if self.question <= len(self.categories_list):
                for elt in self.categories_list:
                    if elt.temp_rank == self.question:
                        self.selected_category = elt
                        self.products.research(self.database, self.tests,\
                        self.substitutes, self.selected_category)
            else:
                print(config.MESSAGE_OOR)
                self.show()
        else:
            system("cls")
            print(config.MESSAGE_OOR)
            self.show()
