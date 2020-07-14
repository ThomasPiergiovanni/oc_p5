#-*-coding:utf-8 -*

import tests
import database
import research
import record
import reset
import stop
import initialisation


class Menu:
    def __init__(self): 
        self.question = None

    def select(self):
        self.question = input("What do you want to do (choose one of the bellow number)?\
        \n 1 - Search for healthier food substitute \
        \n 2 - See your saved substitutes\
        \n 3 - Reinitiate the database \
        \n 4 - Quit the program \n")

    def test(self, database_instance, tests_instance):
        tests.Tests.test_integer(tests_instance, self.question)
        if tests_instance.valid:
            Menu.actions(self, database_instance, tests_instance)
        else:
            print ("Only numbers can be used. Retry ")
            menu_instance = Menu()
            Menu.select(self)

    def actions(self, database_instance, tests_instance) :
        self.question = int(self.question)
        if self.question == 1:
            research.Research.research(self, database_instance)
        elif self.question == 2:
            record.Record.get(database_instance)
        elif self.question == 3:
             reset.Reset.reset(database_instance)
             menu_instance = Menu()
             Menu.select(self)
        elif self.question == 4:
            stop_instance = stop.Stop()
            print("here1")
            stop.Stop.select(stop_instance)
            print("here2")
            stop.Stop.test(stop_instance, tests_instance)

        else :
            print ("Only number from 1 to 4 can be used. Retry ")
            initialisation.Initialisation.initiate()



