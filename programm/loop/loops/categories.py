#-*-coding:utf-8 -*
"""Categories module.
"""
from os import system

from programm.admin import config
from programm.model.category import Category

class Categories:
    """Categories class.
    """
    def __init__(self):
        self.engin = None
        self.database = None
        self.tests = None
        self.products = None
        self.categories_list = []
        self.question = None
        self.selected_category = None

    def reset(self, engin):
        """Method that resets categories into the databse
        (i.e. download data, create table and insert data into table).
        """
        self.engin = engin
        self.database = engin.database
        self.products = engin.products
        self.database.download(self.source())
        self.database.execute_one(self.create_table())
        self.database.execute_many(self.insert_in_table())
        self.set_categories_list(self.database)
        self.products.reset(self.engin)

    def exists(self):
        """Method that provides the sql statement
        for categories existance verification into DB.
        """
        statement = "SELECT * FROM category"
        parameters = [statement, None]
        return parameters

    def source(self):
        """Method that provides the appropriate settings to
        the OFF API for categories download.
        """
        endpoint = config.CATEGORIES_ENDPOINT
        params = {}
        parameters = [endpoint, params]
        return parameters

    def create_table(self):
        """Method that provides the sql statement for
        categories creation into DB.
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
        categories insertion into DB..
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

    def set_categories_list(self, database):
        """Method that create the categories' list.
        """
        self.categories_list.clear()
        database.open_cursor()
        database.cursor.execute("SELECT * FROM category")
        selection = database.cursor.fetchall()
        for elt in selection:
            category = Category(elt[0], elt[1],\
            elt[2], elt[3])
            self.categories_list.append(category)
        database.close_cursor()

    def research(self, engin):
        """Method that starts the categories research loop.
        """
        self.engin = engin
        self.tests = engin.tests
        self.products = engin.products
        self.sort()

    def sort(self):
        """Method that sorts the categories' list per name.
        """
        self.categories_list = sorted(self.categories_list, key=lambda \
        category: category.name)
        self.show()

    def show(self):
        """Method that propose the categories' options to the user.
        """
        print("CATEGORIES:")
        rank = 1
        for elt in self.categories_list:
            elt.temp_rank = rank
            print(elt.temp_rank, " - ", elt.name)
            rank += 1
        self.ask()

    def ask(self):
        """Method that ask to select a category option to the user.
        """
        self.question = input("Which category you want to \
check products for?\n")
        system("cls")
        self.select()

    def select(self):
        """Method that, for the selected category, starts the
        product research loop.
        """
        if self.tests.test_integer(self.question):
            self.question = int(self.question)
            if self.question <= len(self.categories_list):
                for elt in self.categories_list:
                    if elt.temp_rank == self.question:
                        self.selected_category = elt
                        self.products.research(self.engin)
            else:
                print(config.MESSAGE_OOR)
                self.show()
        else:
            print(config.MESSAGE_OOR)
            self.show()
