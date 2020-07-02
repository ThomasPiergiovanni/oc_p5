#-*-coding:utf-8 -*

import urllib.request

import config

class Data:
    def __init__(self):
        self.categories_raw_data = 0

    def get_data(self):
        request = urllib.request.Request(config.CATEGORIES_ENDPOINT, headers = config.HEADER, method = 'GET')
        self.categories_raw_data = urllib.request.urlopen(request)

