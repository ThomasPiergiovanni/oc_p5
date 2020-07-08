#-*-coding:utf-8 

import database

class Reinitialisation:

    def reinitialize(database_instance):
        database.Database.delete(database_instance)
        database.Database.create(database_instance)

