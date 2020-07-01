#-*-coding:utf-8 -*

import urllib.request

class Category:
    def __init__(self):
        self.source_url = 'https://fr-en.openfoodfacts.org/categories.json'
        self.headers = {'User-Agent': 'ThomasApp - Web - Version 0.0'}

    def get_data(self):
        request = urllib.request.Request(self.source_url, headers = self.headers, method = 'GET')
        response = urllib.request.urlopen(request)
        print (response.read())

category_instance = Category()
Category.get_data(category_instance)
