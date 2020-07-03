#-*-coding:utf-8 -*      
import requests
import json

import config


# def get_data():
#     url = "https://fr-en.openfoodfacts.org/category/en:snacks.json"
#     #data = {"page_size": 200}
#     request = urllib.request.Request(url, headers = config.HEADER,  method = 'GET')
#     response = urllib.request.urlopen(request)
#     results = json.load(response)
#     products = results["products"]

def get_data():
    url = "https://fr.openfoodfacts.org/cgi/search.pl"
    params = {
        "action":"process",
        "tagtype_0": "categories",
        "tag_contains_0":"contains",
        "tag_0":"en:breads",
        "json":1,
        "page":1,
        "page_size": 100}
    res= requests.get(url, params = params)
    print(res.status_code)
    print(res.encoding)
    print(res.url)
    results = res.json()

 


    # print(response.status_code)

    products = results["products"]   
    

    for elt in products:
        try:
            if elt["product_name"] and elt["id"]:
                  print (elt["id"], elt["product_name"] )
            else:
                 print("missing")
        except:
            pass

get_data()