#-*-coding:utf-8 -*

import stop

class Abandon:
    def abandon(tests_instance):
        stop_instance = stop.Stop()
        stop.Stop.select(stop_instance)
        stop.Stop.verify(stop_instance, tests_instance)
        stop.Stop.process(stop_instance, tests_instance)