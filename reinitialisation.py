#-*-coding:utf-8 

import database
import download
import categories
import products

class Reinitialisation:

    def reinitialize():
        database_instance = database.Database()
        database.Database.delete(database_instance)
        database.Database.create(database_instance)
        download_instance = download.Download()
        download.Download.categories(download_instance)
        database.Database.insert_categories(database_instance, download_instance)
        categories_instance = categories.Categories()
        categories.Categories.instanciate_category(categories_instance, database_instance)
        for category in categories_instance.categories_list:
            download.Download.products(download_instance, category)
            database.Database.insert_products(database_instance, download_instance,category)
        products_instance = products.Products()
        products.Products.instanciate_product(products_instance, database_instance)

