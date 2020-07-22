#-*-coding:utf-8 -*
from os import system

import sys
from tests import Tests
import menu
import tests

class Abandon:
    def __init__(self, database):
        system("cls")
        self.database = database
        self.question = None
        self.select_input_valid = False
        self.tests = Tests()
        self.select()
        self.execute()

    def select(self):
        self.question = input("Do you really want to quit "\
        "the programm (y/n)?\n")
        self.tests.test_string(self.question)
        if self.tests.valid:
            self.select_input_valid = True

    def execute(self): 
        if self.select_input_valid: 
            self.question = str(self.question)
            if self.question in "yY":
                system("cls")
                sys.exit("Goodbye")
            elif self.question in "nN":
                menu.Menu(self.database)
            else :
                system("cls")
                print ("Only letter y/n can be used. Retry")
                self.select()
                self.execute()
        else:
            system("cls")
            print ("Only letters can be used. Retry")
            self.select()
            self.execute()