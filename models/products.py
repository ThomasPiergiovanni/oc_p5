# -*-coding:utf-8 -*
"""Products module.
"""
from configuration.config import PRODUCTS_ENDPOINT, PRODUCTS_AMOUNT


class Products:
    """Products class.
    """
    def __init__(self):
        self.source = {}
        self.products_list = []

    @classmethod
    def exists(cls):
        """Method that provides the sql statement
        for product table verification into DB.
        """
        statement = "SHOW TABLES LIKE 'product'"
        parameters = [statement, None]
        return parameters

    @classmethod
    def select_all(cls):
        """Method that provides the sql statement
        for selecting all products from DB.
        """
        statement = "SELECT * FROM product"
        parameters = [statement, None]
        return parameters

    @classmethod
    def get_source(cls, category):
        """Method that provides the appropriate settings to
        the OFF API for products download.
        """
        endpoint = PRODUCTS_ENDPOINT
        params = {
            "action": "process", "tagtype_0": "categories",
            "tag_contains_0": "contains", "tag_0": category.id_origin,
            "json": 1, "page": 1, "page_size": PRODUCTS_AMOUNT}
        parameters = [endpoint, params]
        return parameters

    @classmethod
    def create_table(cls):
        """Method that provides the sql statement for
        products creation into DB.
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

    @classmethod
    def insert_in_table(cls):
        """Method that provides the sql statement for
        products insertion into DB.
        """
        statement = "INSERT INTO product (id_origin, product_name,\
        nutriscore_grade, category_id, url, stores)\
        VALUES (%s, %s, %s, %s, %s, %s)"
        parameters = statement
        return parameters
