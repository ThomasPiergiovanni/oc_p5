# -*-coding:utf-8 -*
"""Categories module.
"""
from configuration.config import CATEGORIES_ENDPOINT


class Categories:
    """Categories class.
    """
    def __init__(self):
        self.source = {}
        self.categories_list = []

    @classmethod
    def exists(cls):
        """Method that provides the sql statement
        for category table existance verification into DB.
        """
        statement = "SHOW TABLES LIKE 'category'"
        parameters = [statement, None]
        return parameters

    @classmethod
    def select_all(cls):
        """Method that provides the sql statement
        for selecting all categories from DB.
        """
        statement = "SELECT * FROM category"
        parameters = [statement, None]
        return parameters

    @classmethod
    def get_source(cls):
        """Method that provides the appropriate settings to
        the OFF API for categories download.
        """
        endpoint = CATEGORIES_ENDPOINT
        params = {}
        parameters = [endpoint, params]
        return parameters

    @classmethod
    def create_table(cls):
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

    @classmethod
    def insert_in_table(cls):
        """Method that provides the sql statement for
        categories insertion into DB.
        """
        statement = "INSERT INTO category(id_origin, name,\
            url) VALUES(%s, %s, %s)"
        parameters = statement
        return parameters
