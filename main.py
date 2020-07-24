#-*-coding:utf-8 -*
"""Main module.
"""
from initialization import Initialization

def main():
    """Method lauching the programm.
    """
    initialization = Initialization()
    initialization.initialization_nominal_scenario()

if __name__ == "__main__":
    main()
