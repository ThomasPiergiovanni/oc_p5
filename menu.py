#-*-coding:utf-8 -*

import database
import research
import record
import reset
import quit


class Menu:
    def show (database_instance):
        question = input("What do you want to do (choose one of the bellow number)?\
        \n 1 - Search for healthier food substitute \
        \n 2 - See your saved substitutes\
        \n 3 - Reinitiate the database \
        \n 4 - Quit the program \n")
        try:
            question = int(question)
            if question == 1:
                research.Research.research(database_instance)
                Menu.show(database_i1nstance)
            elif question == 2:
                record.Record.get(database_instance)
                Menu.show(database_instance)
            elif question == 3:
                 reset.Reset.reset(database_instance)
            elif question == 4:
                quit.Quit.show()
            else :
                print ("Only number from 1 to 4 can be used. Retry ")
                Menu.show(database_instance)
        except:
            print ("Only NUMBERS can be used. Retry ")
            Menu.show(database_instance)
