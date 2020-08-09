# -*-coding:utf-8 -*
"""Register module.
"""
from os import system


class Register:
    """Register class.
    """
    def __init__(self):
        self.engine = None
        self.menu = None
        self.records_list = None

    def watch(self, engine):
        """Method that starts register watch.
        """
        self.engine = engine
        self.menu = engine.menu
        self.records_list = engine.records.records_list 
        self.show()

    def show(self):
        """Method that propose/show the records to the user.
        """
        if self.records_list:
            print("Produits & substituts enregistrés:")
            rank = 1
            for elt in self.records_list:
                print(
                    rank, "."
                    "\n    Nom du produit:", elt.product_product_name,
                    "(", elt.product_nutriscore_grade.capitalize(), ")",
                    "\n    Nom du substitut:", elt.substitute_product_name,
                    "(", elt.substitute_nutriscore_grade.capitalize(), ")")
                rank += 1
            system("pause")
            system("cls")
            self.menu.start(self.engine)
        else:
            print("Aucun substitut n'a été enregistrés pour le moment")
            system("pause")
            system("cls")
            self.menu.start(self.engine)