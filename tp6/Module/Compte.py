from Module import Numero_compte
from Module.String_int import String_int


class Compte():

    def __init__(self,parti1:String_int,parti2:int,parti3:int,parti4:int):
        self.compte:Numero_compte=[parti1,(str(parti2)).zfill(4),(str(parti3)).zfill(4),(str(parti4)).zfill(4)]

    def __str__(self):
        return ''.join(str(e) for e in self.compte)