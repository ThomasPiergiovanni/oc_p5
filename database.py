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

    def show_categories(self):
        self.cursor.execute ("SELECT name_origin FROM p5.category ORDER BY name_origin ASC")
        selection = self.cursor.fetchall()
        question = "Select a category:"
        print (question)
        rank = 1
        for elt in selection:
            name_origin = elt[0]
            print (rank," - ", name_origin)
            rank += 1 