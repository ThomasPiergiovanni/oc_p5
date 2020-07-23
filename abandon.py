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
        self.menu = menu.Menu(self.database)
        self.abandon_nominal_scenario()

    def abandon_nominal_scenario(self):
        self.ask()
        self.select()

    def ask(self):
        self.question = input("Do you really want to quit "\
        "the programm (y/n)?\n")
        self.tests.test_string(self.question)
        if self.tests.valid:
            self.select_input_valid = True

    def select(self): 
        if self.select_input_valid: 
            self.question = str(self.question)
            if self.question in "yY":
                system("cls")
                sys.exit("Goodbye")
            elif self.question in "nN":
                self.menu.menu_nominal_scenario()
            else :
                system("cls")
                print ("Only letter y/n can be used. Retry")
                self.abandon_nominal_scenario()
        else:
            system("cls")
            print ("Only letters can be used. Retry")
            self.abandon_nominal_scenario()