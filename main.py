#-*-coding:utf-8 -*

import menu
import database




def main():
    database_instance= database.Database()
    database.Database.create_database(database_instance)
    # database.Database.check_tables(database_instance)
    #database.Database.test(database_instance)
    #menu.Menu.show(database_instance)



if __name__=="__main__":
    main()



