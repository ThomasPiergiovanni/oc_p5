#-*-coding:utf-8 -*
"""Record module.
"""
class Record:
    """Record class.
    """
    def __init__(self, category, product, substitute):
        self.product_id = product.id_product
        self.product_product_name = product.product_name
        self.product_nutriscore_grade = product.nutriscore_grade
        self.product_url = product.url
        self.product_stores = product.stores
        self.product_category_id = product.category_id
        self.category_name = category.name
        self.substitute_id = substitute.id_product
        self.substitute_product_name = substitute.product_name
        self.substitute_nutriscore_grade = substitute.nutriscore_grade
        self.substitute_url = substitute.url
        self.substitute_stores = substitute.stores
