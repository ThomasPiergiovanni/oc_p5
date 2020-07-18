#-*-coding:utf-8 -*


import database
import tests
import menu
import reset

class Initialisation:
    def initiate():
        database_instance = database.Database()
        database.Database.check(database_instance)
        if database_instance.status:
            menu_instance = menu.Menu()
            menu.Menu.select(menu_instance)
            menu.Menu.execute(menu_instance, database_instance)
        else:
            reset.Reset()
            Initialisation.inititate()