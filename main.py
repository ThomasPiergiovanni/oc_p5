#-*-coding:utf-8 -*
"""Main module.
"""
from programm.engin import Engin

def main():
    """Method lauching the programm.
    """
    engin = Engin()
    engin.initialize_database()

if __name__ == "__main__":
    main()
