#-*-coding:utf-8 -*

from database import Database
from menu import Menu
from reset import Reset

class Initialisation:
    def __init__(self):
        self.database = Database()
        self.initiate()

    def initiate(self):
        self.database.check()
        if self.database.status:
            Menu(self.database)
        else:
            Reset(self.database)