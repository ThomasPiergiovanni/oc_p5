#-*-coding:utf-8 
import requests

import config

class Download:
    def __init__(self):
        self.source_categories = {}
        self.source_products = {}

    def categories(self):
        try:
            response_api =requests.get(config.CATEGORIES_ENDPOINT,\
            headers = config.HEADER )
            self.source_categories = response_api.json()
        except HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
        except Exception as other_error:
            print(f"Other error occurred: {other_error}")
        else:
            print("HTTP call to API for categories successfull")

    def products(self, category):
        try:
            params = {
                "action":"process", "tagtype_0": "categories",
                "tag_contains_0":"contains", "tag_0":category.id_origin,
                "json":1, "page":1, "page_size": config.PRODUCTS_AMOUNT}
            response_api =requests.get(config.PRODUCTS_ENDPOINT,\
            headers = config.HEADER, params = params)
            self.source_products = response_api.json()
        except HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
        except Exception as other_error:
            print(f"Other error occurred: {other_error}")
        else:
            print(f"HTTP call to API for {category.id_origin} successfull")