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
        self.database.verify(self.database.para1, self.database.para2)
        print (self.database.status)
        if self.database.status:
            self.database.execute_one(self.database.use())
            self.database.content()
            if self.database.status:
                Menu(self.database)
            else:
                Reset(self.database)
        else:
            Reset(self.database)