#-*-coding:utf-8 -*


import database
import tests
import menu
import reset

class Initialisation:
    def initiate():
        database_instance= database.Database()
        database.Database.check(database_instance)
        tests_instance = tests.Tests()
        if database_instance.status:
            menu_instance = menu.Menu()
            menu.Menu.select(menu_instance)
            menu.Menu.verify(menu_instance, tests_instance)
            menu.Menu.process(menu_instance, database_instance, tests_instance)
        else:
            reset.Reset.reset(database_instance)
            Initialisation.inititate()