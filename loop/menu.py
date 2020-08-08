# -*-coding:utf-8 -*
"""Menu module
"""
from os import system

from configuration.config import MESSAGE_OOR


class Menu:
    """Menu class.
    """
    def __init__(self):
        self.engine = None
        self.tests = None
        self.database = None
        self.categories = None
        self.records = None
        self.abandon = None
        self.question = None

    def start(self, engine):
        """Method that starts the menu loop.
        """
        self.engine = engine
        self.tests = engine.tests
        self.database = engine.database
        self.categories = engine.categories
        self.records = engine.records
        self.abandon = engine.abandon
        self.show()

    def show(self):
        """Method that proposes the menus' options to the user.
        """
        system("cls")
        print("Menu:"
              "\n 1 - Chercher des produits alimentaires de substitution"
              " plus sain."
              "\n 2 - Regarder les substituts déja enregistrés."
              "\n 3 - Ré-initialiser la base de données."
              "\n 4 - Quitter le programme.")
        self.ask()

    def ask(self):
        """Method that ask to select a menu option to the user.
        """
        self.question = input("Que voulez-vous faire"
                              " (Entrez le nombre correspondant à votre"
                              " choix)?\n")
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
                print(MESSAGE_OOR)
                self.start(self.engine)
        else:
            print(MESSAGE_OOR)
            self.start(self.engine)
