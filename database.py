#-*-coding:utf-8 -*
import requests

import mysql.connector

import config

class Database:
    def __init__(self): 
        self.connection = mysql.connector.connect\
        (host = config.HOST, user = config.USER,\
        password = config.PASSWORD)
        self.status = False
        self.statement = None
        self.source_categories = {}
        self.source_products = {}

    def download_categories(self):
        try:
            response_api =requests.get(config.CATEGORIES_ENDPOINT,\
            headers = config.HEADER )
            self.source_categories = response_api.json()
        except HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
        except Exception as other_error:
            print(f"Other error occurred: {other_error}")
        else:
            print("HTTP call to API for categories successfull")

    def download_products(self, category):
        try:
            params = {
                "action":"process", "tagtype_0": "categories",
                "tag_contains_0":"contains", "tag_0":category.id_origin,
                "json":1, "page":1, "page_size": config.PRODUCTS_AMOUNT}
            response_api =requests.get(config.PRODUCTS_ENDPOINT,\
            headers = config.HEADER, params = params)
            self.source_products = response_api.json()
        except HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
        except Exception as other_error:
            print(f"Other error occurred: {other_error}")
        else:
            print(f"HTTP call to API for {category.id_origin} successfull")

    def set_database(self):
        self.statement = "USE %s"% config.DATABASE_NAME
        return self.statement
        
    def close_connection_to_db(self):
        self.connection.close()

    def open_cursor(self):
        self.cursor = self.connection.cursor()

    def close_cursor(self):
        self.cursor.close()

    def execute_one(self, statement):
        self.open_cursor()
        self.cursor.execute(statement)
        self.connection.commit()
        self.close_cursor()

    def exists(self):
        try:
            self.open_cursor()
            self.cursor.execute("SHOW DATABASES LIKE '%s'"% config.DATABASE_NAME)
            self.cursor.fetchall()
            if self.cursor.rowcount >= 1:
                self.status = True
            self.close_cursor()
        except:
            self.status = False
            print("No DB")

    def content(self):
        querries = ("category","product")
        try: 
            for querry in querries:
                self.open_cursor()
                self.cursor.execute("SELECT * FROM %s"% querry)
                self.cursor.fetchall()
                if self.cursor.rowcount >= 1:
                    self.status = True
                self.close_cursor()
        except:
            self.status = False
            print ("No or empty tables")

    def create_db(self):
        statement = "CREATE DATABASE IF NOT EXISTS %s CHARACTER\
        SET 'utf8';"% config.DATABASE_NAME
        return statement

    def delete_db(self):
        statement = "DROP DATABASE IF EXISTS %s"% config.DATABASE_NAME
        return statement

    def create(self):
        self.open_cursor()
        with open(config.SQL_FILE, "r") as file:
            content = file.read()
            querries = content.split(";")
            for querry in querries:
                self.cursor.execute(querry)
        self.close_cursor()



    def insert_categories(self):
        self.open_cursor()
        statement = "INSERT INTO category (id_origin, name,\
        url) VALUES (%s, %s, %s)"
        value = []
        for elt in self.source_categories["tags"]:
            if elt["id"] in config.SELECTED_CATEGORIES and elt["name"] and\
            elt["url"]:
                elt_string = (elt["id"], elt["name"], elt["url"])
                value.append(elt_string)
            else:
                pass
        self.cursor.executemany(statement, value)
        self.connection.commit()
        self.close_cursor()

    def insert_products(self, category):
        self.open_cursor()
        statement = "INSERT INTO product (id_origin, product_name,\
        nutriscore_grade, category_id, url, stores)\
        VALUES (%s, %s, %s, %s, %s, %s)"
        value = []
        for elt in self.source_products["products"]:
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
        self.close_cursor()

