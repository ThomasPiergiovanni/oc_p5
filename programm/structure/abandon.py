#-*-coding:utf-8 -*
"""Abandon module.
"""
from os import system
from sys import exit

from programm.admin import config
from programm.structure import menu
from programm.admin.tests import Tests

class Abandon:
    """Abandon class.
    """
    def __init__(self, database):
        system("cls")
        self.database = database
        self.menu = menu.Menu(self.database)
        self.question = None
        self.tests = Tests()
        self.abandon_nominal_scenario()

    def abandon_nominal_scenario(self):
        """Method that starts the programm abandon
        nominal scenario.
        """
        self.ask()
        self.select()

    def ask(self):
        """Method that propose the abandon confirmation
        options to the user.
        """
        self.question = input("Do you really want to quit "\
        "the programm (y/n)?\n")
        self.tests.test_string(self.question)

    def select(self):
        """Method that starts the selected option.
        """
        if self.tests.valid:
            self.question = str(self.question)
            if self.question in "yY":
                system("cls")
                exit("Goodbye")
            elif self.question in "nN":
                system("cls")
                self.menu.menu_nominal_scenario()
            else:
                system("cls")
                print(config.MESSAGE_YN)
                self.abandon_nominal_scenario()
        else:
            system("cls")
            print(config.MESSAGE_YN)
            self.abandon_nominal_scenario()
