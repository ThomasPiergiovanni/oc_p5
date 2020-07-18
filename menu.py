#-*-coding:utf-8 -*

import tests
import database
import research
import record
import reset
import abandon
import initialisation


class Menu:
    def __init__(self): 
        self.question = None
        self.select_input_valid = False

    def process (self, database_instance):
        self.select()
        self.execute(database_instance)

    def select(self):
        self.question = input("What do you want to do (choose one of the bellow number)?\
        \n 1 - Search for healthier food substitute \
        \n 2 - See your saved substitutes\
        \n 3 - Reinitiate the database \
        \n 4 - Quit the program \n")
        tests_instance = tests.Tests()
        tests.Tests.test_integer(tests_instance, self.question)
        if tests_instance.valid:
            self.select_input_valid = True

    def execute(self, database_instance) :
        if self.select_input_valid:
            self.question = int(self.question)
            if self.question == 1:
                research.Research()
            elif self.question == 2:
                record.Record()
            elif self.question == 3:
                reset.Reset()
            elif self.question == 4:
                abandon.Abandon()
            else :
                print ("Only number from 1 to 4 can be used. Retry ")
                initialisation.Initialisation.initiate()
        else:
            print("Only numbers can be used. Retry")
            initialisation.Initialisation.initiate()


