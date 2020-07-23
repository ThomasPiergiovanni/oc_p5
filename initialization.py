#-*-coding:utf-8 -*

from database import Database

class Initialization:
    def __init__(self):
        self.database = Database()
        self.database.initialization_nominal_scenario()