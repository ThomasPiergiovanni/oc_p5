#-*-coding:utf-8 -*
import urllib.request
import json
import operator

import config


class Products():
    def __init__(self):
        self.source_data = []
        self.products_list = []

    def get_data(self,categories_instance):
        for elt in categories_instance.wanted_categories:
            url = config.PRODUCTS_ENDPOINT_BEGINNING + elt.id + config.PRODUCTS_ENDPOINT_END
            request = urllib.request.Request(url, headers = config.HEADER, method = 'GET')
            response = urllib.request.urlopen(request)
            self.source_data = json.load(response)

    def initialize(self, categories_instance):
        for elt in self.source_data["products"]:
            id = elt["id"]
            product_name = elt["product_name"]
            url = elt["url"]
            countries = elt["countries"]
            countries_tag = elt["countries_tag"]
            nutriscore_grade = elt["nutriscore_grade"]
            stores = elt["stores"]
            purchase_places = elt["purchase_places"]
            purchase_places_tags = elt["purchase_places_tags"]
            category_id = elt["category"]
            countries_tag = elt["countries_tag"]
        #     products = elt["products"]
        #     category_instance = category.Category(id, name, url, products)
        #     self.categories_list.append(category_instance)
