#-*-coding:utf-8 -*

class Category:
    def __init__(self, id_category, id_origin, name, url):
        self.id_category = id_category
        self.id_origin = id_origin
        self.name = name
        self.url = url
        self.temp_rank = None
