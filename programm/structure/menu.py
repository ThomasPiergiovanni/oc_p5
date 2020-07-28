#-*-coding:utf-8 -*
"""Menu module
"""
from os import system

from programm.admin import config
# from programm.structure.record import Record
# from programm.structure.reset import Reset


class Menu:
    """Menu class.
    """
    def __init__(self):
        self.question = None

    def start_menu(self, engin):
        """Method that starts the menu
        nominal scenario.
        """
        self.engin = engin
        self.database = engin.database
        self.tests = engin.tests
        self.categories = engin.categories
        self.compositions = engin.compositions
        self.abandon = engin.abandon
        self.show()

    def show(self):
        """Method that propose the menu options to the user.
        """
        system("cls")
        print("MENU:\
        \n 1 - Search for healthier food substitute \
        \n 2 - See your saved substitutes\
        \n 3 - Reinitiate the database \
        \n 4 - Quit the program")
        self.ask()

    def ask(self):
        """Method that ask for menu's option selection to the user.
        """
        self.question = input("What do you want to do \
(choose one of the above number)?\n")
        self.select()

    def select(self):
        """Method that starts the selected option.
        """
        if self.tests.test_integer(self.question):
            self.question = int(self.question)
            if self.question == 1:
                system("cls")
                self.categories.research(self.engin)
            elif self.question == 2:
                self.compositions.start_record(self.engin)
            elif self.question == 3:
                self.database.reset(self.engin)
            elif self.question == 4:
                self.abandon.start_abandon(self.engin)
            else:
                system("cls")
                print(config.MESSAGE_OOR)
                self.start_menu(self.engin)
        else:
            system("cls")
            print(config.MESSAGE_OOR)
            self.start_menu(self.engin)
