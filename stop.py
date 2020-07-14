#-*-coding:utf-8 -*

import initialisation
import tests

class Stop:
    def __init__(self):
        self.question = None

    def select(self):
        self.question = input("Do you want to really want to quit\
        the programm (y/n)?\n")

    def test (self, tests_instance):
        tests.Tests.test_string(tests_instance, self.question)
        if tests_instance.valid:
            Stop.action(self)
        else:
            print ("Only letter can be used. Retry ")
            stop_instance = Stop()
            Stop.select(self)

    def action(self):       
        self.question = str(self.question)
        if self.question in "yY":
            print ("Goodbye")
        elif self.question in "nN":
            initialisation.Initialisation.initiate()
        else :
            print ("Only letter y/n can be used. Retry ")
            Stop.action(self)