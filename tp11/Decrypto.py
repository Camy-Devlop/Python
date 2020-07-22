from Constant import Constant

class Decrypto():

    def __init__(self, cle:int):
        self.cle:int=cle
        self.lor=Constant().lor

    def test(self):
        pass


d=Decrypto(2.3)
d.test()