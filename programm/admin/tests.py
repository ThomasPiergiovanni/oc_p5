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
        """Method that test if input product got values for
        the specified attributes
        """
        for product in products:
            try:
                if product["id"] and product["product_name"] and\
                    product["nutriscore_grade"] and product["url"]:
                    consistent_product = (product["id"],\
                    product["product_name"], product["nutriscore_grade"],\
                    category.id_category, product["url"], product["stores"])
                    self.consistent_products.append(consistent_product)
            except Exception as error:
                # print(f"The following error occurred: {error}")
                pass
    def test_duplicate(self, products):
        """Method that test if input products are unique per id and category.
        """
        for product in products:
            unique_pairs = []
            pair = (product[0], product[3])
            if pair not in unique_pairs:
                unique_pairs.append(pair)
                self.unique_products.append(product)
