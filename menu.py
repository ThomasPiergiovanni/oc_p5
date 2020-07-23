#-*-coding:utf-8 -*
from os import system

from tests import Tests
from research import Research
from record import Record
from reset import Reset
from abandon import Abandon


class Menu:
    def __init__(self, database):
        self.database = database
        self.question = None
        self.select_input_valid = False
        self.tests = Tests()

    def menu_nominal_scenario(self):
        system("cls")
        self.ask()
        self.select()

    def ask(self):
        self.question = input("What do you want to do (choose one of the bellow number)?\
        \n 1 - Search for healthier food substitute \
        \n 2 - See your saved substitutes\
        \n 3 - Reinitiate the database \
        \n 4 - Quit the program \n")
        self.tests.test_integer(self.question)
        if self.tests.valid:
            self.select_input_valid = True

    def select(self) :
        if self.select_input_valid:
            self.question = int(self.question)
            if self.question == 1:
                Research(self.database)
            elif self.question == 2:
                Record(self.database)
            elif self.question == 3:
                Reset(self.database)
            elif self.question == 4:
                Abandon(self.database)
            else :
                system("cls")
                print ("Only number from 1 to 4 can be used. Retry ")
                self.menu_nominal_scenario()
        else:
            system("cls")
            print("Only numbers can be used. Retry")
            self.menu_nominal_scenario()


