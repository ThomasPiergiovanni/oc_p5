#-*-coding:utf-8 -*
import mysql.connector

import config

class Database:
    def __init__(self):   
        self.connection = mysql.connector.connect\
        (host = config.HOST, user = config.USER, password = config.PASSWORD)
        self.cursor = self.connection.cursor()
        self.database_status = False
        self.tables_status = False


    def check_database(self):

        self.cursor.execute("SHOW DATABASES")
        databases = self.cursor.fetchall()
        database_exists = [database[0] for database in databases if database[0] == "p5"]
        if database_exists:
            self.database_status = True

    def check_tables (self):
        querries = ("category","product")
        for querry in querries:
            self.cursor.execute("SELECT * FROM p5.%s"% querry)
            self.cursor.fetchall()
            if self.cursor.rowcount > 1:
                self.tables_status = True

        print (self.tables_status)

    def create(self):
        with open(config.SQL_FILE, "r") as file:
            content = file.read()
            querries = content.split(";")
            for querry in querries:
                self.cursor.execute(querry)

    def delete(self):
        statement = "DROP DATABASE IF EXISTS p5"
        self.cursor.execute(statement)
        self.connection.commit()

    def insert_categories(self, download_instance):
        statement = "INSERT INTO p5.category (id_origin, name,\
        url) VALUES (%s, %s, %s)"
        value = []
        for elt in download_instance.source_categories["tags"]:
            if elt["id"] in config.SELECTED_CATEGORIES and elt["name"] and\
            elt["url"]:
                elt_string = (elt["id"], elt["name"], elt["url"])
                value.append(elt_string)
            else:
                pass
        self.cursor.executemany(statement, value)
        self.connection.commit()

    def insert_products(self, download_instance, category):
        statement = "INSERT INTO p5.product (id_origin, product_name,\
        nutriscore_grade, category_id, url, stores)\
        VALUES (%s, %s, %s, %s, %s, %s)"
        value = []
        for elt in download_instance.source_products["products"]:
            try: 
                if elt["id"] and elt["product_name"] and\
                elt["nutriscore_grade"] and elt["url"]:
                    elt_string = (elt["id"], elt["product_name"],\
                    elt["nutriscore_grade"], category.id_category,\
                    elt["url"], elt["stores"])
                    value.append(elt_string)
            except Exception as error:
                print(f"The following error occurred: {error}")
                pass
        self.cursor.executemany(statement, value)
        self.connection.commit()

    def insert_substitute(self,  products_instance, substitutes_instance):
        if substitutes_instance.registration:
            statement = "INSERT INTO p5.substitute (product_product_id,\
            substitute_product_id) VALUES (%s, %s)"
            value = [products_instance.selected_product, substitutes_instance.selected_substitute]
            self.cursor.execute(statement, value)
            self.connection.commit() 



