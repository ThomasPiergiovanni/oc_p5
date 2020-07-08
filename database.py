#-*-coding:utf-8 -*
import mysql.connector

import config

class Database:
    def __init__(self):   
        self.database = mysql.connector.connect\
        (host = config.HOST, user = config.USER, password = config.PASSWORD)
        self.cursor = self.database.cursor()

    def create(self):
        with open(config.SQL_FILE, "r") as file:
            content = file.read()
            querries = content.split(";")
            for querry in querries:
                self.cursor.execute(querry)

    def delete(self):
        statement = "DROP DATABASE IF EXISTS p5"
        self.cursor.execute(statement)
        self.database.commit()

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
        self.database.commit()

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
        self.database.commit()



