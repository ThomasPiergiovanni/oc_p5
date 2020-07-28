#-*-coding:utf-8 -*
"""Abandon module.
"""
from os import system
from sys import exit

from programm.admin import config

class Abandon:
    """Abandon class.
    """
    def __init__(self):
        self.engin = None
        self.database = None
        self.tests = None
        self.menu = None
        self.question = None

    def abandon(self, engin):
        """Method that starts the programm abandon
        nominal scenario.
        """
        self.engin = engin
        self.database = engin.database
        self.tests = engin.tests
        self.menu = engin.menu
        self.ask()

    def ask(self):
        """Method that propose the abandon confirmation
        options to the user.
        """
        system("cls")
        self.question = input("Do you really want to quit "\
        "the programm (y/n)?\n")
        self.select()

    def select(self):
        """Method that starts the selected option.
        """
        system("cls")
        if self.tests.test_string(self.question):
            self.question = str(self.question)
            if self.question in "yY":
                exit("Goodbye")
            elif self.question in "nN":
                self.menu.start_menu(self.engin)
            else:
                print(config.MESSAGE_YN)
                self.ask()
        else:
            print(config.MESSAGE_YN)
            self.ask()
