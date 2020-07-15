#-*-coding:utf-8 -*

import stop

class Abandon:
    def abandon():
        stop_instance = stop.Stop()
        stop.Stop.select(stop_instance)
        stop.Stop.execute(stop_instance)