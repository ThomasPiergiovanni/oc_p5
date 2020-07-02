#-*-coding:utf-8 -*

import urllib.request
import json

import config
import category

class Categories:
    def __init__(self):
        self.source_data = {}
        self.categories_list=[]

    def get_data(self):
        request = urllib.request.Request(config.CATEGORIES_ENDPOINT, headers = config.HEADER, method = 'GET')
        response = urllib.request.urlopen(request)
        self.source_data = json.load(response)

    def initialize (self):
        for elt in self.source_data["tags"]:
            id = elt["id"]
            name = elt["name"]
            url = elt["url"]
            products = elt["products"]
            category_instance = category.Category(id, name, url, products)
            self.categories_list.append(category_instance)


        #print (self.categories_raw_data["tags"][0])



categories_instance = Categories()
Categories.get_data(categories_instance)
Categories.initialize(categories_instance)

for elt in categories_instance.categories_list:
    if elt.id == "fr:produit-marin":
        print(elt.id)