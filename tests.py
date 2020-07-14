#-*-coding:utf-8 -*      

class Tests:
    def __init__(self):
        self.valid = False

    def test_integer(self, value):
        try:
            value = int(value)
            self.valid = True
        except:
            self.valid = False

    def test_string(self, value):
        try:
            value = str(value)
            self.valid = True
        except:
            self.valid = False
