#-*-coding:utf-8 -*

class Product:
    def __init__(self, id_product, id_origin, product_name_origin, nutriscore_grade_origin, category_id):
        self.id_product = id_product
        self.id_origin = id_origin
        self.product_name_origin = product_name_origin
        self.nutriscore_grade_origin = nutriscore_grade_origin
        self.category_id = category_id
