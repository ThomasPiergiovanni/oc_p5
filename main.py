#-*-coding:utf-8 -*

import database
import reset
import research


def main():
    database_instance = database.Database()
    # reset.Reset.reset(database_instance)
    research.Research.research(database_instance)


main()



