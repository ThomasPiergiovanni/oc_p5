#-*-coding:utf-8 -*

import database
import research
import registration
import reset
import quit



def main():
    database_instance = database.Database()

    # research.Research.research(database_instance)

    # registration.Registration.regi(database_instance)

    # reset.Reset.reset(database_instance)

    quit.Quit.show()


if __name__=="__main__":
    main()



