#-*-coding:utf-8 -*

import database
import categories
import products


database_instance = database.Database()
database.Database.create(database_instance) 

categories_instance = categories.Categories()
categories.Categories.get_data(categories_instance)
categories.Categories.insert(categories_instance, database_instance)
categories.Categories.instanciate_category(categories_instance, database_instance)

products_instance = products.Products()
for category in categories_instance.categories_list:
    products.Products.get_data(products_instance, category)
    products.Products.insert(products_instance, database_instance, category)
    products.Products.instanciate_product(products_instance, database_instance)

    # products.Products.insert(products_instance, database_instance)



#products.Product.initialize(database_instance.selected_categories)
