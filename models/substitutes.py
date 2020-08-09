# -*-coding:utf-8 -*
"""Substitutes module.
"""
from configuration.config import MESSAGE_OOR, MESSAGE_YN


class Substitutes:
    """Substitutes class.
    """
    def __init__(self): 
        self.substitutes_list = []

    @classmethod
    def exists(cls):
        """Method that provides the sql statement
        for product table verification into DB.
        """
        statement = "SHOW TABLES LIKE 'substitute'"
        parameters = [statement, None]
        return parameters

    @classmethod
    def select_all(cls):
        """Method that provides the sql statement
        for selecting all substitutes from DB.
        """
        statement = "SELECT * FROM substitute"
        parameters = [statement, None]
        return parameters

    @classmethod
    def create_table(cls):
        """Method that provides the sql statement for
        substitutes creation into DB.
        """
        statement = "CREATE TABLE IF NOT EXISTS substitute(\
            product_id SMALLINT UNSIGNED NOT NULL,\
            substitute_id SMALLINT UNSIGNED NOT NULL,\
            FOREIGN KEY (product_id) REFERENCES product(id_product),\
            FOREIGN KEY (substitute_id) REFERENCES product(id_product)\
            )ENGINE=INNODB;"
        parameters = [statement, None]
        return parameters
        
    @classmethod
    def insert_in_table(cls):
        """Method that provides the sql statement for
        substitute insertion into DB.
        """
        statement = "INSERT INTO substitute (\
            product_id, substitute_id) VALUES (%s, %s)"
        parameters = statement
        return parameters
