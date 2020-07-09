#-*-coding:utf-8 -*

import database
import reinitialisation
import research


def main():
    database_instance = database.Database()
    # reinitialisation.Reinitialisation.reinitialize(database_instance)
    research.Research.research(database_instance)


main()



