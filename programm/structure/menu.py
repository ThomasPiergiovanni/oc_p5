#-*-coding:utf-8 -*
"""Menu module
"""
from os import system

from programm.admin import config
from programm.structure.abandon import Abandon
from programm.structure.record import Record
from programm.structure.research import Research
from programm.structure.reset import Reset
from programm.admin.tests import Tests

class Menu:
    """Menu class.
    """
    def __init__(self, database):
        self.database = database
        self.question = None
        self.select_input_valid = False
        self.tests = Tests()

    def menu_nominal_scenario(self):
        """Method that starts the menu
        nominal scenario.
        """
        self.show()
        self.ask()
        self.select()

    def show(self):
        """Method that propose the menu options to the user.
        """
        print("MENU:\
        \n 1 - Search for healthier food substitute \
        \n 2 - See your saved substitutes\
        \n 3 - Reinitiate the database \
        \n 4 - Quit the program")

    def ask(self):
        """Method that ask for menu's option selection to the user.
        """
        self.question = input("What do you want to do \
(choose one of the above number)?\n")
        self.tests.test_integer(self.question)

    def select(self):
        """Method that starts the selected option.
        """
        if self.tests.valid:
            self.question = int(self.question)
            if self.question == 1:
                Research(self.database)
            elif self.question == 2:
                Record(self.database)
            elif self.question == 3:
                Reset(self.database)
            elif self.question == 4:
                Abandon(self.database)
            else:
                system("cls")
                print(config.MESSAGE_OOR)
                self.menu_nominal_scenario()
        else:
            system("cls")
            print(config.MESSAGE_OOR)
            self.menu_nominal_scenario()
