#-*-coding:utf-8 -*
"""Abandon module.
"""
from os import system
from sys import exit

from tests import Tests
# import menu

class Abandon:
    """Abandon class.
    """
    def __init__(self, database):
        system("cls")
        self.database = database
        self.question = None
        self.select_input_valid = False
        self.tests = Tests()
        # self.menu = menu.Menu(self.database)
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
        if self.tests.valid:
            self.select_input_valid = True

    def select(self):
        """Method that starts the selected option.
        """
        if self.select_input_valid:
            self.question = str(self.question)
            if self.question in "yY":
                system("cls")
                exit("Goodbye")
            elif self.question in "nN":
                from menu import Menu
                self.menu = Menu(self.database)
                self.menu.menu_nominal_scenario()
            else:
                system("cls")
                print("Only letter y/n can be used. Retry")
                self.abandon_nominal_scenario()
        else:
            system("cls")
            print("Only letters can be used. Retry")
            self.abandon_nominal_scenario()
