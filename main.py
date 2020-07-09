#-*-coding:utf-8 -*

import database
import research
import registration
import reset



def main():
    database_instance = database.Database()

    # research.Research.research(database_instance)

    registration.Registration.registration(database_instance)

    # reset.Reset.reset(database_instance)


main()



