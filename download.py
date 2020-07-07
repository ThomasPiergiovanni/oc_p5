#-*-coding:utf-8 
import requests

import config

class Download:
    def __init__(self):
        self.source_categories = {}

    def categories(self):
        try:
            response_api =requests.get(config.CATEGORIES_ENDPOINT,\
            headers = config.HEADER )
            self.source_categories = response_api.json()
        except HTTPError as http_error:
            print(f'HTTP error occurred: {http_error}')
        except Exception as other_error:
            print(f'Other error occurred: {other_error}')
        else:
            print('HTTP call to API for categories successfull')