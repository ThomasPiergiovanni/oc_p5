#-*-coding:utf-8 -*
"""Tests module.
"""
class Tests:
    """Tests class.
    """
    def __init__(self):
        self.valid = False
        self.consistent_products = []
        self.unique_products = []

    def test_integer(self, value):
        """Method that test if input is a number
        """
        if value.isnumeric():
            self.valid = True
        else:
            self.valid = False
        return self.valid


    def test_string(self, value):
        """Method that test if is an alphabetic character
        """
        if value.isalpha():
            self.valid = True
        else:
            self.valid = False
        return self.valid

    def test_consistency(self, products, category):
        """Method that filter-in only OFF API products that got values for
        id, product_name, nutriscore_grade and url attributes.
        """
        self.consistent_products.clear()
        for product in products:
            try:
                if product["id"] and product["product_name"] and\
                    product["nutriscore_grade"] and product["url"]:
                    consistent_product = (product["id"],\
                    product["product_name"], product["nutriscore_grade"],\
                    category.id_category, product["url"], product["stores"])
                    self.consistent_products.append(consistent_product)
            except KeyError:
                pass
        self.test_duplicate()

    def test_duplicate(self):
        """Method that filter-in only OFF API products that are
        unique per name and id_category.
        """
        self.unique_products.clear()
        product_tuples_list = []
        for product in self.consistent_products:
            product_tuple = (product[1], product[3])
            if product_tuple not in product_tuples_list:
                product_tuples_list.append(product_tuple)
                self.unique_products.append(product)
