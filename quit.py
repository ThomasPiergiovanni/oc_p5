#-*-coding:utf-8 -*

import main

class Quit:
    def show():
        question = input("Do you want to really want to quit the programm (y/n)?")
        question = str(question)
        if question in "yY":
            print("Good bye !") 
        elif question in "nN":
            main.main()
        else :
            print ("Only letter y/n can be used. Retry ")
            Quit.show()