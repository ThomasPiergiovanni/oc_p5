#-*-coding:utf-8 -*
import sys
import initialisation
import tests

class Stop:
    def __init__(self):
        self.question = None

    def select(self):
        self.question = input("Do you really want to quit "\
        "the programm (y/n)?\n")

    def verify (self, tests_instance):
        tests.Tests.test_string(tests_instance, self.question)

    def process (self, tests_instance):
        if tests_instance.valid:
            Stop.actions(self)
        else:
            print ("Only letters can be used. Retry")
            initialisation.Initialisation.initiate()

    def actions(self):       
        self.question = str(self.question)
        if self.question in "yY":
            sys.exit("Goodbye")
        elif self.question in "nN":
            initialisation.Initialisation.initiate()
        else :
            print ("Only letter y/n can be used. Retry")
            initialisation.Initialisation.initiate()