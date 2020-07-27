#-*-coding:utf-8 -*
"""Menu module
"""
from os import system

from programm.admin import config
# from programm.structure.abandon import Abandon
# from programm.structure.record import Record
# from programm.structure.research import Research
# from programm.structure.reset import Reset
# from programm.admin.tests import Tests

class Menu:
    """Menu class.
    """
    def __init__(self):
        self.question = None

    def menu_nominal_scenario(self, database, tests, categories, products,\
    substitutes, compositions):
        """Method that starts the menu
        nominal scenario.
        """
        self.show()
        self.ask()
        self.select(database, tests, categories, products,\
        substitutes, compositions)
        
    def show(self):
        """Method that propose the menu options to the user.
        """
        system("cls")
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

    def select(self, database, tests, categories, products,\
    substitutes, compositions):
        """Method that starts the selected option.
        """
        if tests.test_integer(self.question):
            self.question = int(self.question)
            if self.question == 1:
                system("cls")
                categories.research(database, tests, products,\
                substitutes)
            # elif self.question == 2:
            #     Record(database)
            # elif self.question == 3:
            #     Reset(database)
            # elif self.question == 4:
            #     Abandon(database)
            else:
                system("cls")
                print(config.MESSAGE_OOR)
                self.menu_nominal_scenario(database, tests, categories, products,\
                substitutes, compositions)
        else:
            system("cls")
            print(config.MESSAGE_OOR)
            self.menu_nominal_scenario(database, tests, categories, products,\
            substitutes, compositions)
