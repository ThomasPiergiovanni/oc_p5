# -*-coding:utf-8 -*
"""Engine module.
"""
from controllers.connection_manager import ConnectionManager
from models.categories import Categories
from models.database import Database
from models.mapper.record import Record
from models.products import Products
from models.records import Records
from models.substitutes import Substitutes
from verification.tests import Tests
from views.abandon import Abandon
from views.menu import Menu
from views.abandon import Abandon
from views.register import Register
from views.research import Research


class Engine:
    """Engine class.
    """
    def __init__(self):
        self.connection_manager = ConnectionManager()
        self.abandon = Abandon()
        self.database = Database()
        self.records = Records()
        self.categories = Categories()
        self.products = Products()
        self.substitutes = Substitutes()
        self.abandon = Abandon()
        self.menu = Menu()
        self.register = Register()
        self.research = Research()
        self.tests = Tests()
        self.initialize_database()

    def initialize_database(self):
        """Method that initialize the database. It checks if
        the DB exists and  its tables exists.
        - If it does, the program "datas" are strored into a list and the
        Menu program is started.
        - If it don't, the database and its componnents are created.
        """
        if self.connection_manager.verify(self.database.exists()):
            self.connection_manager.execute_one(self.database.use())
            if self.connection_manager.verify(
                    self.categories.exists()) and \
                    self.connection_manager.verify(
                        self.products.exists()) and \
                    self.connection_manager.verify(
                        self.substitutes.exists()):
                if self.connection_manager.verify(
                        self.categories.select_all()) and\
                        self.connection_manager.verify(
                            self.products.select_all()):
                    self.set_datas_list()
                    self.menu.start(self)
                else:
                    self.reinitialize_database()
            else:
                self.reinitialize_database()
        else:
            self.reinitialize_database()

    def reinitialize_database(self):
        """Method that resets the database (i.e. drop, create and use DB).
        """
        self.connection_manager.execute_one(self.database.delete())
        self.connection_manager.execute_one(self.database.create())
        self.connection_manager.execute_one(self.database.use())
        self.reinitialize_categories()

    def reinitialize_categories(self):
        """Method that resets categories into the database
        (i.e. download data, create table and insert data into table).
        """
        self.connection_manager.execute_one(
            self.categories.create_table())
        self.connection_manager.download(
            self,
            self.categories.get_source())
        self.tests.test_categories_consistency(
             self.categories.source["tags"])
        self.connection_manager.execute_many(
            [self.categories.insert_in_table(),
            self.tests.consistent_categories])
        self.connection_manager.set_categories_list(
            self,
            self.categories.select_all())
        self.reinitialize_products()

    def reinitialize_products(self):
        """Method that resets products into the database
        (i.e. download data, create table and insert data into table).
        """
        self.connection_manager.execute_one(
            self.products.create_table())
        for category in self.categories.categories_list:
            self.connection_manager.download(
                self,
                self.products.get_source(category))
            self.tests.test_products_consistency(
                self.products.source["products"],
                category)
            self.connection_manager.execute_many(
                [self.products.insert_in_table(),
                self.tests.unique_products])
        self.reinitialize_substitutes()

    def reinitialize_substitutes(self):
        """Method that resets substitutes into the database
        (i.e. create table) and re-set all datas (i.e. reset
        all datas into their respective list).
        """
        self.connection_manager.execute_one(
            self.substitutes.create_table())
        self.set_datas_list()
        self.menu.start(self)

    def add_substitute_in_db(self, product_id, substitute_id):
        parameters = [
            self.substitutes.insert_in_table(), [product_id, substitute_id]]
        self.connection_manager.execute_one(parameters)
        self.set_datas_list()

    def set_datas_list(self):
        """Method that sets datas into their
        respective list.
        """
        self.connection_manager.set_categories_list(
            self, self.categories.select_all())
        self.connection_manager.set_products_list(
            self, self.products.select_all())
        self.connection_manager.set_substitutes_list(
            self, self.substitutes.select_all())
        self.set_records_list()

    def set_records_list(self):
        """Method that create the records' list.
        """
        self.records.records_list.clear()
        for substitute in self.substitutes.substitutes_list:
            self.product = [
                product for product in self.products.products_list
                if product.id_product == substitute.product_id]
            self.substitute = [
                product for product in self.products.products_list
                if product.id_product == substitute.substitute_id]
            self.category = [
                category for category in self.categories.categories_list
                if category.id_category == self.product[0].category_id]
            record = Record(
                self.category[0], self.product[0], self.substitute[0])
            self.records.records_list.append(record)
