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

    def insert_categories(self, download_instance):
        statement = "INSERT INTO category (id_origin, name,\
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


