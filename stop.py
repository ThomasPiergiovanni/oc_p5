#-*-coding:utf-8 -*
import sys
import initialisation
import tests

class Stop:
    def __init__(self):
        self.question = None
        self.select_input_valid = False

    def select(self):
        self.question = input("Do you really want to quit "\
        "the programm (y/n)?\n")
        tests_instance = tests.Tests()
        tests.Tests.test_string(tests_instance, self.question)
        if tests_instance.valid:
            self.select_input_valid = True

    def execute(self): 
        if self.select_input_valid:     
            self.question = str(self.question)
            if self.question in "yY":
                sys.exit("Goodbye")
            elif self.question in "nN":
                initialisation.Initialisation.initiate()
            else :
                print ("Only letter y/n can be used. Retry")
                initialisation.Initialisation.initiate()
        else:
            print ("Only letters can be used. Retry")
            initialisation.Initialisation.initiate()