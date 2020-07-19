#-*-coding:utf-8 -*
import mysql.connector

import config

class Database:
    def __init__(self):   
        self.my_database = mysql.connector.connect\
        (host = config.HOST, user = config.USER, password = config.PASSWORD)
        self.status = False

    def open_cursor(self):
        self.cursor = self.my_database.cursor()

    def close_cursor(self):
        self.cursor.close()

    def check(self):
        querries = ("category","product")
        try: 
            for querry in querries:
                self.open_cursor()
                self.cursor.execute("SELECT * FROM p5.%s"% querry)
                self.cursor.fetchall()
                if self.cursor.rowcount > 1:
                    self.status = True
                self.close_cursor()
        except:
            self.status = False
            print ("bug")

    def create(self):
        with open(config.SQL_FILE, "r") as file:
            self.open_cursor()
            content = file.read()
            querries = content.split(";")
            for querry in querries:
                self.cursor.execute(querry)
            self.close_cursor()

    def delete(self):
        if self.status == False:
            self.open_cursor()
            statement = "DROP DATABASE IF EXISTS p5;"
            self.cursor.execute(statement)
            self.my_database.commit()
            self.close_cursor()

            


    def insert_categories(self, download):
        self.open_cursor()
        statement = "INSERT INTO p5.category (id_origin, name,\
        url) VALUES (%s, %s, %s)"
        value = []
        for elt in download.source_categories["tags"]:
            if elt["id"] in config.SELECTED_CATEGORIES and elt["name"] and\
            elt["url"]:
                elt_string = (elt["id"], elt["name"], elt["url"])
                value.append(elt_string)
            else:
                pass
        self.cursor.executemany(statement, value)
        self.my_database.commit()
        self.close_cursor()

    def insert_products(self, category, download):
        self.open_cursor()
        statement = "INSERT INTO p5.product (id_origin, product_name,\
        nutriscore_grade, category_id, url, stores)\
        VALUES (%s, %s, %s, %s, %s, %s)"
        value = []
        for elt in download.source_products["products"]:
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
        self.my_database.commit()
        self.close_cursor()

