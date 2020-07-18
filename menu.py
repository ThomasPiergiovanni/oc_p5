#-*-coding:utf-8 -*

from tests import Tests
import research
import record
import reset
import abandon
import initialisation


class Menu:
    def __init__(self): 
        self.question = None
        self.select_input_valid = False
        self.tests = Tests()
        self.select()
        self.execute()


    def select(self):
        self.question = input("What do you want to do (choose one of the bellow number)?\
        \n 1 - Search for healthier food substitute \
        \n 2 - See your saved substitutes\
        \n 3 - Reinitiate the database \
        \n 4 - Quit the program \n")
        self.tests.test_integer(self.question)
        if self.tests.valid:
            self.select_input_valid = True

    def execute(self) :
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
                initialisation.Initialisation()
        else:
            print("Only numbers can be used. Retry")
            initialisation.Initialisation()


