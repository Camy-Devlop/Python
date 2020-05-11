class Numero_compte(object):

    def __init__(self,numero:str):
        if len(numero)==16:
            self.compte=numero
            self.parti4:str
        else:
            print("erreur compte invalide")

    def couper(self):
        c:str
        cpt:int=0
        for e in list(self.compte):
            if cpt<=4:
                c+=e
                cpt+=1
