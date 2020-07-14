#-*-coding:utf-8 -*

import menu
import database
import main
import sys

class Quit:
    def show():
        question = input("Do you want to really want to quit the programm (y/n)?")
        question = str(question)
        if question in "yY":
            print ("Goodbye")
        elif question in "nN":
            database_instance= database.Database()
            menu.Menu.show(database_instance)
        else :
            print ("Only letter y/n can be used. Retry ")
            Quit.show()