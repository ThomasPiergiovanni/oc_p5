# -*-coding:utf-8 -*
"""Research module.
"""
from os import system

from configuration.config import MESSAGE_OOR, MESSAGE_YN


class Research:
    """Research class.
    """
    def __init__(self):
        self.engine = None
        self.connection_manager = None
        self.tests = None
        self.products = None
        self.substitutes = None
        self.categories_list = []
        self.selected_category = None
        self.products_list = []
        self.selected_products = []
        self.selected_product = None
        self.menu = None
        self.selected_substitutes = []
        self.selected_substitute = None
        self.registration = False
        self.substitutes_registered_list = []
        self.question = None

    def start_research(self, engine):
        """Method that starts the categories research.
        """
        self.engine = engine
        self.tests = engine.tests
        self.menu = engine.menu
        self.categories_list = engine.categories.categories_list
        self.products_list = engine.products.products_list
        self.substitutes = engine.substitutes
        self.connection_manager = engine.connection_manager
        self.sort_categories()

    def sort_categories(self):
        """Method that sorts the categories' list per name.
        """
        self.categories_list = sorted(
            self.categories_list, key=lambda category: category.name)
        self.show_categories()

    def show_categories(self):
        """Method that propose the categories' options to the user.
        """
        print("Catégories:")
        rank = 1
        for elt in self.categories_list:
            elt.temp_rank = rank
            print(elt.temp_rank, " - ", elt.name)
            rank += 1
        self.ask_categories()

    def ask_categories(self):
        """Method that ask to select a category option to the user.
        """
        self.question = input(
            "Quelle catégorie de produits voulez-vous"
            " choisir?\n")
        system("cls")
        self.select_categories()

    def select_categories(self):
        """Method that, for the selected category, starts the
        products research.
        """
        if self.tests.test_integer(self.question):
            self.question = int(self.question)
            if self.question <= len(self.categories_list):
                for elt in self.categories_list:
                    if elt.temp_rank == self.question:
                        self.selected_category = elt
                        self.find_products()
            else:
                print(MESSAGE_OOR)
                self.show_categories()
        else:
            print(MESSAGE_OOR)
            self.show_categories()

    def find_products(self):
        """Method that find and store in a list products that
        belong to the pre-selected category.
        """
        self.selected_products.clear()
        for elt in self.products_list:
            if elt.category_id == self.selected_category.id_category:
                self.selected_products.append(elt)
        self.sort_products()

    def sort_products(self):
        """Method that sorts the wanted category products
        per products name.
        """
        self.selected_products = sorted(
            self.selected_products, key=lambda product: product.product_name)
        self.show_products()

    def show_products(self):
        """Method that propose the products' options to the user.
        """
        print(
            "Vous cherchez un produit dans la catégorie \"",
            self.selected_category.name, "\"")
        print(
            "Produit (Nutriscore):")
        rank = 1
        for elt in self.selected_products:
            elt.temp_product_rank = rank
            print(
                elt.temp_product_rank, " - ", elt.product_name, "(",
                elt.nutriscore_grade.capitalize(), ")")
            rank += 1
        self.ask_products()

    def ask_products(self):
        """Method that ask to select a product option to the user.
        """
        self.question = input(
            "Pour quel produit cherchez-vous un substitut?\n")
        system("cls")
        self.select_product()

    def select_product(self):
        """Method that, for the selected product, starts the
        substitutes research.
        """
        if self.tests.test_integer(self.question):
            self.question = int(self.question)
            if self.question <= len(self.selected_products):
                for elt in self.selected_products:
                    if elt.temp_product_rank == self.question:
                        self.selected_product = elt
                        self.find_substitutes()
            else:
                print(MESSAGE_OOR)
                self.show_products()
        else:
            print(MESSAGE_OOR)
            self.show_products()

    def find_substitutes(self):
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
        self.sort_substitutes()

    def sort_substitutes(self):
        """Method that sorts the wanted product substitutes
        per substitutes name.
        """
        if self.selected_substitutes:
            self.selected_substitutes = sorted(
                self.selected_substitutes,
                key=lambda product: product.nutriscore_grade)
            self.show_substitutes()
        else:
            print("Il n'y a pas de substitut plus sain pour ce produit.")
            system("pause")
            system("cls")
            self.menu.start(self.engine)

    def show_substitutes(self):
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
        self.ask_substitutes()

    def ask_substitutes(self):
        """Method that ask to select a substitute option to the user.
        """
        self.question = input("Quel substituts choisissez vous?\n")
        system("cls")
        self.select_substitutes()

    def select_substitutes(self):
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
                        self.ask_registration_substitutes()
            else:
                print(MESSAGE_OOR)
                self.show_substitutes()
        else:
            print(MESSAGE_OOR)
            self.show_substitutes()

    def ask_registration_substitutes(self):
        """Method that ask to register substitutes to the user.
        """
        self.question = input("Voulez-vous enregistrer votre choix(o/n)?\n")
        system("cls")
        self.select_registration_substitutes()

    def select_registration_substitutes(self):
        """Method that starts the selected option (i.e. register the
        substitute or not).
        """
        if self.tests.test_string(self.question):
            self.question = str(self.question)
            if self.question in "oO":
                self.engine.add_substitute_in_db(
                    self.selected_product.id_product,
                    self.selected_substitute.id_product)
                print("Le substitut a été enregistré!")
                system("pause")
                self.menu.start(self.engine)
            elif self.question in "nN":
                print("Le substitut n\'a pas été enregistré.")
                system("pause")
                self.menu.start(self.engine)
            else:
                print(MESSAGE_YN)
                self.ask_registration_substitutes()
        else:
            print(MESSAGE_YN)
            self.ask_registration_substitutes()
