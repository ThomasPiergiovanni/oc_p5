#-*-coding:utf-8 -*

import menu
import database




def main():
    database_instance= database.Database()

    database.Database.check_database(database_instance)
    database.Database.check_tables(database_instance)

    if database_instance.database_status or\
    database_instance.table_status:
        menu.Menu.show(database_instance)
    else:
        reset.Reset.reset(database_instance)




if __name__=="__main__":
    main()



