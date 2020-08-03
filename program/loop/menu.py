#-*-coding:utf-8 -*
"""Menu module
"""
from os import system

from program.admin import config

class Menu:
    """Menu class.
    """
    def __init__(self):
        self.engine = None
        self.database = None
        self.tests = None
        self.categories = None
        self.records = None
        self.abandon = None
        self.question = None

    def start(self, engine):
        """Method that starts the menu loop.
        """
        self.engine = engine
        self.database = engine.database
        self.tests = engine.tests
        self.categories = engine.categories
        self.records = engine.records
        self.abandon = engine.abandon
        self.show()

    def show(self):
        """Method that proposes the menus' options to the user.
        """
        system("cls")
        print("MENU:\
        \n 1 - Search for healthier food substitute. \
        \n 2 - See your saved substitutes.\
        \n 3 - Reinitiate the database. \
        \n 4 - Quit the program.")
        self.ask()

    def ask(self):
        """Method that ask to select a menu option to the user.
        """
        self.question = input("What do you want to do \
(choose one of the above number)?\n")
        system("cls")
        self.select()

    def select(self):
        """Method that starts the selected option loop.
        """
        if self.tests.test_integer(self.question):
            self.question = int(self.question)
            if self.question == 1:
                self.categories.research(self.engine)
            elif self.question == 2:
                self.records.watch(self.engine)
            elif self.question == 3:
                self.database.reset(self.engine)
            elif self.question == 4:
                self.abandon.start(self.engine)
            else:
                print(config.MESSAGE_OOR)
                self.start(self.engine)
        else:
            print(config.MESSAGE_OOR)
            self.start(self.engine)
