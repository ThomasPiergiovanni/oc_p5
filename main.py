#-*-coding:utf-8 -*

import database
import categories


database_instance = database.Database()
database.Database.create(database_instance) 

categories_instance = categories.Categories()
categories.Categories.get_data(categories_instance)
categories.Categories.initialize(categories_instance)

database.Database.insert_categories(database_instance, categories_instance.categories_list)

selected_categories = database.Database.select_categories(database_instance)
