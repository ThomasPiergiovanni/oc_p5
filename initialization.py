#-*-coding:utf-8 -*

from database import Database

# from reset import Reset

class Initialization:
    def __init__(self):
        self.database = Database()
        self.database.initialization_nominal_scenario()
        # self.initiate()

    # def initiate(self):
    #     self.database.verify(self.database.exists())
    #     if self.database.status:
    #         self.database.execute_one(self.database.use())
    #         self.database.verify(self.categories.exists())
    #         self.database.verify(self.products.exists())
    #         if self.database.status:
    #             self.menu.menu_nominal_scenario()
    #         else:
    #             Reset(self.database)
    #     else:
    #         Reset(self.database)

