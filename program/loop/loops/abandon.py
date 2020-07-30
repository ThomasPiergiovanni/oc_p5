#-*-coding:utf-8 -*
"""Abandon module.
"""
from os import system
from sys import exit

from program.admin import config

class Abandon:
    """Abandon class.
    """
    def __init__(self):
        self.engin = None
        self.database = None
        self.tests = None
        self.menu = None
        self.question = None

    def start(self, engin):
        """Method that starts the abandon loop.
        """
        self.engin = engin
        self.database = engin.database
        self.tests = engin.tests
        self.menu = engin.menu
        self.ask()

    def ask(self):
        """Method that ask to confirm program abandon
        to the user.
        """
        self.question = input("Do you really want to quit "\
        "the program (y/n)?\n")
        system("cls")
        self.select()

    def select(self):
        """Method that starts the selected option (i.e. leave
        the program or not).
        """
        if self.tests.test_string(self.question):
            self.question = str(self.question)
            if self.question in "yY":
                exit("Goodbye")
            elif self.question in "nN":
                self.menu.start(self.engin)
                system("cls")
            else:
                print(config.MESSAGE_YN)
                self.ask()
        else:
            print(config.MESSAGE_YN)
            self.ask()
