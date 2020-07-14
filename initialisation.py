#-*-coding:utf-8 -*

import menu
import database

class Initilaisation:
    def initiate():
        database_instance= database.Database()
        database.Database.check(database_instance)
        if database_instance.status:
            menu.Menu.show(database_instance)
        else:
            reset.Reset.reset(database_instance)