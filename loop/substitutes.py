# -*-coding:utf-8 -*
"""Substitutes module.
"""
from os import system

from configuration.config import MESSAGE_OOR, MESSAGE_YN
from model.substitute import Substitute


class Substitutes:
    """Substitutes class.
    """
    def __init__(self):
        self.engine = None
        self.database = None
        self.tests = None
        self.menu = None
        self.selected_products = None
        self.selected_product = None
        self.selected_substitutes = []
        self.question = None
        self.selected_substitute = None
        self.registration = False
        self.substitutes_registered_list = []

    def reset(self, engine):
        """Method that resets substitutes into the database
        (i.e. create table) and re-set all datas (i.e. reset
        all datas into their respective list).
        """
        self.engine = engine
        self.database = engine.database
        self.menu = engine.menu
        self.database.execute_one(self.create_table())
        self.engine.set_datas()
        self.menu.start(self.engine)

    @classmethod
    def exists(cls):
        """Method that provides the sql statement
        for product table verification into DB.
        """
        statement = "SHOW TABLES LIKE 'substitute'"
        parameters = [statement, None]
        return parameters

    @classmethod
    def create_table(cls):
        """Method that provides the sql statement for
        substitutes creation into DB.
        """
        statement = "CREATE TABLE IF NOT EXISTS substitute(\
            product_id SMALLINT UNSIGNED NOT NULL,\
            substitute_id SMALLINT UNSIGNED NOT NULL,\
            FOREIGN KEY (product_id) REFERENCES product(id_product),\
            FOREIGN KEY (substitute_id) REFERENCES product(id_product)\
            )ENGINE=INNODB;"
        parameters = [statement, None]
        return parameters

    def set_substitutes_list(self, database):
        """Method that create the substitutes' list.
        """
        self.substitutes_registered_list.clear()
        database.open_cursor()
        database.cursor.execute("SELECT * FROM substitute")
        selection = database.cursor.fetchall()
        for elt in selection:
            substitute = Substitute(elt[0], elt[1])
            self.substitutes_registered_list.append(substitute)
        database.close_cursor()

    def research(self, engine):
        """Method that starts the substitutes research.
        """
        self.engine = engine
        self.database = engine.database
        self.tests = engine.tests
        self.menu = engine.menu
        self.selected_products = engine.products.selected_products
        self.selected_product = engine.products.selected_product
        self.find()

    def find(self):
        """Method that find and store in a list, substitutes that
        belong to the same category as the pre-selected product but
        that have a better nutriticore.
        """
        self.selected_substitutes.clear()
        for elt in self.selected_products:
            if elt.id_product != self.selected_product.id_product and \
                    elt.nutriscore_grade < \
                    self.selected_product.nutriscore_grade:
                self.selected_substitutes.append(elt)
        self.sort()

    def sort(self):
        """Method that sorts the wanted product substitutes
        per substitutes name.
        """
        if self.selected_substitutes:
            self.selected_substitutes = sorted(
                self.selected_substitutes,
                key=lambda product: product.nutriscore_grade)
            self.show()
        else:
            print("Il n'y a pas de substitut plus sain pour ce produit.")
            system("pause")
            system("cls")
            self.menu.start(self.engine)

    def show(self):
        """Method that propose the substitutes' options to the user.
        """
        print(
            "Vous cherchez un substitut pour le produit \"",
            self.selected_product.product_name, "(",
            self.selected_product.nutriscore_grade.capitalize(), ")", "\"")
        print("Substituts (Nutriscore):")
        rank = 1
        for elt in self.selected_substitutes:
            elt.temp_substitute_rank = rank
            print(
                elt.temp_substitute_rank, " - ", elt.product_name, "(",
                elt.nutriscore_grade.capitalize(), ")")
            rank += 1
        self.ask()

    def ask(self):
        """Method that ask to select a substitute option to the user.
        """
        self.question = input("Quel substituts choisissez vous?\n")
        system("cls")
        self.select()

    def select(self):
        """Method that, for the selected substitutes, starts the
        substitutes registration.
        """
        if self.tests.test_integer(self.question):
            self.question = int(self.question)
            if self.question <= len(self.selected_substitutes):
                for elt in self.selected_substitutes:
                    if elt.temp_substitute_rank == self.question:
                        print(
                            "Vous avez choisi le substitut suivant:",
                            "\n   - Nom du produit:", elt.product_name,
                            "\n   - Nutriscore:",
                            elt.nutriscore_grade.capitalize(),
                            "\n   - Infos disponibles sur:", elt.url,
                            "\n   - Vendu chez:", elt.stores)
                        self.selected_substitute = elt
                        self.ask_registration()
            else:
                print(MESSAGE_OOR)
                self.show()
        else:
            print(MESSAGE_OOR)
            self.show()

    def ask_registration(self):
        """Method that ask to register substitutes to the user.
        """
        self.question = input("Voulez-vous enregistrer votre choix(o/n)?\n")
        system("cls")
        self.select_registration()

    def select_registration(self):
        """Method that starts the selected option (i.e. register the
        substitute or not).
        """
        if self.tests.test_string(self.question):
            self.question = str(self.question)
            if self.question in "oO":
                self.registration = True
                self.database.execute_one(self.insert_in_table())
                self.engine.set_datas()
                print("Le substitut a été enregistré!")
                system("pause")
                self.menu.start(self.engine)
            elif self.question in "nN":
                print("Le substitut n\'a pas été enregistré.")
                system("pause")
                self.menu.start(self.engine)
            else:
                print(MESSAGE_YN)
                self.ask_registration()
        else:
            print(MESSAGE_YN)
            self.ask_registration()

    def insert_in_table(self):
        """Method that provides the sql statement for
        substitute insertion into DB.
        """
        if self.registration:
            statement = "INSERT INTO substitute (\
                product_id, substitute_id) VALUES (%s, %s)"
            values = [
                self.selected_product.id_product,
                self.selected_substitute.id_product]
            parameters = [statement, values]
        return parameters
