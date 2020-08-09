# -*-coding:utf-8 -*
"""Database module.
"""
from configuration.env import DATABASE_NAME


class Database:
    """Database class.
    """
    @classmethod
    def exists(cls):
        """Method that provides the sql statement
        for DB existance verification.
        """
        statement = "SHOW DATABASES LIKE '%s'" % DATABASE_NAME
        parameters = [statement, None]
        return parameters

    @classmethod
    def delete(cls):
        """Method that provides the sql statement for
        DB deletion.
        """
        statement = "DROP DATABASE IF EXISTS %s" % DATABASE_NAME
        parameters = [statement, None]
        return parameters

    @classmethod
    def create(cls):
        """Method that provides the sql statement for
        DB creation.
        """
        statement = "CREATE DATABASE IF NOT EXISTS %s CHARACTER\
        SET 'utf8';" % DATABASE_NAME
        parameters = [statement, None]
        return parameters

    @classmethod
    def use(cls):
        """Method that sets the appropriate database to use for
        the program.
        """
        statement = "USE %s" % DATABASE_NAME
        parameters = [statement, None]
        return parameters
