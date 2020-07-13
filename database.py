#-*-coding:utf-8 -*
import mysql.connector

import config

class Database:
    def __init__(self):   
        self.connection = mysql.connector.connect\
        (host = config.HOST, user = config.USER, password = config.PASSWORD)
        self.cursor = self.connection.cursor()
        self.tables_rows_list =[]

    def test(self):
        for table in self.tables_rows_list:
            table_rows = table [0][0]
            table_rows = int(table_rows)

            print (table_rows)
        # if result > 1:
        #     print ("category ok")
        # else:
        #     print ("bug")


    def check_tables (self):
        querries = ("category","product")
        for querry in querries:
            # statement ="SELECT * FROM p5.%s"
            # value = querry.replace("\"","")
            self.cursor.execute("SELECT * FROM p5.%s"% querry)
            self.cursor.fetchall()
            result = self.cursor.rowcount
            print(result)
            #self.tables_rows_list.append (result)

        # querries = ["SELECT * FROM p5.category", "SELECT * FROM p5.product"]
        # for querry in querries:
        #     self.cursor.execute(querry)
        #     self.cursor.fetchall()
        #     result = self.cursor.rowcount
        #     print(result)
        #     #self.tables_rows_list.append (result)


    def check_product (self):
        check = "SELECT * FROM p5.product"
        self.cursor.execute(check)
        self.cursor.fetchall()
        result = self.cursor.rowcount
        print(result)

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



