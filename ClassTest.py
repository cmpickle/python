__author__ = 'cmpickle'


class Test(object):

    test = ""

    def __init__(self, quote):
        self.test = quote

    def to_string(self):
        print(self.test)

    @staticmethod
    def interstellar():
        print("Do not go gently into that good night. Rage, rage against the dying of the light.")