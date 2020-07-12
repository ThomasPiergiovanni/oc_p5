#-*-coding:utf-8 -*

import menu
import database




def main():
    database_instance= database.Database()
    menu.Menu.show(database_instance)



if __name__=="__main__":
    main()



