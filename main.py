#-*-coding:utf-8 -*

import database
import categories
import products


database_instance = database.Database()
database.Database.create(database_instance) 

categories_instance = categories.Categories()
categories.Categories.get_data(categories_instance)
categories.Categories.initialize(categories_instance)

database.Database.insert_categories(database_instance, categories_instance.categories_list)

database.Database.select_categories(database_instance)

products_instance = products.Products()
products.Products.get_data(products_instance, database_instance.selected_categories)
#products.Product.initialize(database_instance.selected_categories)
