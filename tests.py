#-*-coding:utf-8 -*      

class Tests:
    def __init__(self):
        self.valid = False

    def test_integer(self, value):
        if value.isnumeric():
            self.valid = True
        else:
            self.valid = False

    def test_string(self, value):
        if value.isalpha():
            self.valid = True
        else:
            self.valid = False
