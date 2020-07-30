#-*-coding:utf-8 -*
"""Main module.
"""
from program.engin import Engin

def main():
    """Main method launching the program.
    """
    engin = Engin()
    engin.initialize_database()

if __name__ == "__main__":
    main()
