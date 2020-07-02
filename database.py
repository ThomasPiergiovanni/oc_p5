#-*-coding:utf-8 -*
import mysql.connector
import config

class Database:
    def __init__(self):   
        self.database = mysql.connector.connect\
        (host = config.HOST, user = config.USER, password = config.PASSWORD)
        self.cursor = self.database.cursor()
        self.selected_categories= []

    def create(self):
        with open(config.SQL_FILE, "r") as file:
            content = file.read()
            querries = content.split(";")
            for querry in querries:
                self.cursor.execute(querry)

    def insert_categories (self, categories):
        statement = "INSERT INTO category (id_origin, name_origin,\
         url_origin, products_origin) VALUES (%s, %s, %s,%s)"
        value = []
        for elt in categories:
            if elt.id and elt.name and elt.url and elt.products:
                elt_string = (elt.id, elt.name, elt.url, elt.products)
                value.append(elt_string)
            else:
                pass
        self.cursor.executemany(statement, value)
        self.database.commit()

    def select_categories(self):
        self.cursor.execute ("SELECT * FROM category WHERE category.id_origin IN\
         (%s,%s,%s,%s,%s) ", config.SELECTED_CATEGORIES)
        self.selected_categories = self.cursor.fetchall()

        for elt in self.selected_categories:
            print (elt)


        #print(self.cursor.rowcount, "was inserted.")


