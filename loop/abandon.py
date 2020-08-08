#-*-coding:utf-8 -*
"""Abandon module.
"""
from os import system
from sys import exit as leave_program

from admin.config import MESSAGE_YN

class Abandon:
    """Abandon class.
    """
    def __init__(self):
        self.engine = None
        self.tests = None
        self.menu = None
        self.question = None

    def start(self, engine):
        """Method that starts the abandon loop.
        """
        self.engine = engine
        self.tests = engine.tests
        self.menu = engine.menu
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
                leave_program("Goodbye")
            elif self.question in "nN":
                self.menu.start(self.engine)
                system("cls")
            else:
                print(MESSAGE_YN)
                self.ask()
        else:
            print(MESSAGE_YN)
            self.ask()
