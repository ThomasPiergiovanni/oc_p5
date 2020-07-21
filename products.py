#-*-coding:utf-8 -*

from os import system
import config

from database import Database
from categories import Categories
from product import Product
from tests import Tests


class Products():
    def __init__(self, database):
        # system("cls")
        self.database = database
        self.source_data = {}
        self.products_list = []
        self.selected_products = []
        self.sorted_products = []
        self.question = None
        self.tests = Tests()
        self.select_input_valid = False
        self.selected_product = 0

    def exists(self):
        statement = "SELECT * FROM product"
        message= "No or empty product tables"
        parameters = [statement, message]
        return parameters

    def source(self, category):
        endpoint = config.PRODUCTS_ENDPOINT
        params = {
                "action":"process", "tagtype_0": "categories",
                "tag_contains_0":"contains", "tag_0":category.id_origin,
                "json":1, "page":1, "page_size": config.PRODUCTS_AMOUNT}
        parameters = [endpoint, params]
        return parameters

    def create_table(self):
        statement = "CREATE TABLE IF NOT EXISTS product(\
            id_product SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,\
            id_origin VARCHAR(250) NOT NULL,\
            product_name VARCHAR(250) NOT NULL,\
            nutriscore_grade VARCHAR(250) NOT NULL,\
            category_id SMALLINT UNSIGNED NOT NULL,\
            url LONGTEXT NOT NULL,\
            stores VARCHAR(250),\
            PRIMARY KEY (id_product),\
            FOREIGN KEY (category_id) REFERENCES category(id_category)\
            )ENGINE=INNODB;"
        return statement

    def insert_in_table(self, category):
        statement = "INSERT INTO product (id_origin, product_name,\
        nutriscore_grade, category_id, url, stores)\
        VALUES (%s, %s, %s, %s, %s, %s)"
        values = []
        for elt in self.database.source["products"]:
            try: 
                if elt["id"] and elt["product_name"] and\
                elt["nutriscore_grade"] and elt["url"]:
                    elt_string = (elt["id"], elt["product_name"],\
                    elt["nutriscore_grade"], category.id_category,\
                    elt["url"], elt["stores"])
                    values.append(elt_string)
            except Exception as error:
                print(f"The following error occurred: {error}")
                pass
        parameters = [statement, values]
        return parameters

    def instanciate(self):
        self.database.open_cursor()
        self.database.cursor.execute ("SELECT * FROM product")
        selection = self.database.cursor.fetchall()   
        for elt in selection:
            product = Product(elt[0], elt[1],elt[2], elt[3], elt[4],\
            elt[5], elt[6])        
            self.products_list.append(product)
        self.database.close_cursor()

    def process (self, categories):
        self.organize(categories)
        self.show()
        self.select()
        self.execute(categories)

    def organize(self, categories):
        for elt in self.products_list:
            if elt.category_id == categories.selected_category.id_category:
                self.selected_products.append(elt)
                self.sorted_products = sorted(self.selected_products, key = lambda \
                product : product.product_name)

    def show(self):
        print ("PRODUCTS:")
        rank = 1
        for elt in self.sorted_products:
            elt.temp_product_rank = rank
            print (elt.temp_product_rank ," - ",elt.product_name)
            rank += 1 

    def select(self):
        self.question= input("Which product you want to find a substitute for?\n")
        self.tests.test_integer(self.question)
        if self.tests.valid:
            self.select_input_valid = True

    def execute(self, categories):
        if self.select_input_valid:
            self.question = int(self.question)
            if self.question <= len(self.selected_products):
                for elt in self.selected_products:
                    if elt.temp_product_rank == self.question:
                        print ("You\'ve choosen the \"", elt.product_name, "\" product") 
                        self.selected_product = elt
            else:
                system("cls")
                print ("Only numbers included in above list can be used. Retry")
                self.show()
                self.select()
                self.execute(categories)
        else:
            system("cls")
            print ("Only numbers can be used. Retry")
            self.show()
            self.select()
            self.execute(categories)



       