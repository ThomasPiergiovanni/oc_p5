#-*-coding:utf-8 -*

import database
import reinitialisation
import search


def main():
    database_instance = database.Database()
    # reinitialisation.Reinitialisation.reinitialize(database_instance)
    search.Search.search(database_instance)


main()



