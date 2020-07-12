#-*-coding:utf-8 -*

import database
import research
import registration
import reset
import quit

class Menu:
    def show (database_instance):
        print ("1 - Search for healthier food substitute")
        print ("2 - See your saved substitutes")
        print ("3 - Reinitiate the database")
        print ("4 - Quit the program")
        question = input("What do you want to do (type a number in the list)?")
        question = int(question)
        if question == 1:
            research.Research.research(database_instance)
        elif question == 2:
            registration.Registration.regi(database_instance)
        elif question == 3:
            registration.Registration.regi(database_instance)
        elif question == 4:
            reset.Reset.reset(database_instance)
        else :
            print ("Only letter 1, 2, 3 or 4 can be used. Retry ")
            Menu.show()