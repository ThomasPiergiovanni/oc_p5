#-*-coding:utf-8 -*
"""Product module.
"""
class Product:
    """Product class.
    """
    def __init__(self, id_product, id_origin, product_name,\
    nutriscore_grade, category_id, url, stores):
        self.id_product = id_product
        self.id_origin = id_origin
        self.product_name = product_name
        self.nutriscore_grade = nutriscore_grade
        self.category_id = category_id
        self.url = url
        self.stores = stores
        self.temp_product_rank = None
        self.temp_substitute_rank = None
