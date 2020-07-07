#-*-coding:utf-8 -*

class Product:
    def __init__(self,\
    id_product,\
    id_origin,\
    product_name,\
    nutriscore_grade,\
    category_id,\
    categories_origin,\
    countries_origin,\
    stores_origin):
        self.id_product = id_product
        self.id_origin = id_origin
        self.product_name = product_name
        self.nutriscore_grade = nutriscore_grade
        self.category_id = category_id
        self.categories_origin = categories_origin
        self.countries_origin = countries_origin
        self.stores_origin = stores_origin
