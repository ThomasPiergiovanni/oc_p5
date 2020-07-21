#-*-coding:utf-8 -*

from database import Database
from menu import Menu
from reset import Reset

class Initialisation:
    def __init__(self):
        self.database = Database()
        self.initiate()

    def initiate(self):
        self.database.exists()
        if self.database.status:
            self.database.execute_one(self.database.set_db())
            self.database.content()
            if self.database.status:
                Menu(self.database)
            else:
                Reset(self.database)
        else:
            Reset(self.database)