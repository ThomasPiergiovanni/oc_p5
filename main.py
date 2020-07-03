#-*-coding:utf-8 -*

import database
import categories
import products


database_instance = database.Database()
database.Database.create(database_instance) 

categories_instance = categories.Categories()
categories.Categories.get_data(categories_instance)
categories.Categories.initialize(categories_instance)

categories.Categories.insert(categories_instance, database_instance)
categories.Categories.wanted(categories_instance)

products_instance = products.Products()
products.Products.get_data(products_instance, categories_instance)
#products.Product.initialize(database_instance.selected_categories)
