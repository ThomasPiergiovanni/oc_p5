#-*-coding:utf-8 -*

import urllib.request
import json
import operator

import config
import category

class Categories:
    def __init__(self):
        self.source_data = []
        self.categories_list=[]

    def get_data(self):
        request = urllib.request.Request(config.CATEGORIES_ENDPOINT, headers = config.HEADER, method = 'GET')
        response = urllib.request.urlopen(request)
        self.source_data = json.load(response)

    def initialize(self):
        for elt in self.source_data["tags"]:
            id = elt["id"]
            name = elt["name"]
            url = elt["url"]
            products = elt["products"]
            category_instance = category.Category(id, name, url, products)
            self.categories_list.append(category_instance)

