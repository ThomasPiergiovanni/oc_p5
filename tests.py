#-*-coding:utf-8 -*      

class Tests:
    def __init__(self):
        self.valid = False
        self.consistent_products =[]

    def test_integer(self, value):
        if value.isnumeric():
            self.valid = True
        else:
            self.valid = False

    def test_string(self, value):
        if value.isalpha():
            self.valid = True
        else:
            self.valid = False

    def test_consistency (self, products, category):
        for product in products:
            try:
                if product["id"] and product["product_name"] and\
                    product["nutriscore_grade"] and product["url"]:
                    consistent_product = (product["id"], product["product_name"],\
                    product["nutriscore_grade"], category.id_category,\
                    product["url"], product["stores"])
                    self.consistent_products.append(consistent_product)
            except Exception as error:
                print(f"The following error occurred: {error}")
                pass
