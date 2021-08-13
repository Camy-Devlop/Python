from mot import Mot
class Compte_mot():
    __texte: str
    __mots = dict()
    __caractaire_speciaux = "1234567890@#&\"\'(§!)-_^¨*$€%£?,;./:+=®†œπ‡∂¬µ≤‹≈©◊ß~∞…÷≠¥∏ŒÆŸªΩ∆|‰≥›√∫±\ • ¿´”’[]«»Ø]–"

    def traitement_text(self):
        tmp = self.__texte.split(" ")

        for i in tmp:
            i=self.__nettoyage(i)
            if i.lower() not in self.__mots.keys():
                self.__mots[i.lower()]=Mot(i)
            else:
                self.__mots[i.lower()].mot=i
           # print("mot:{0},nombre de fois {1}".format(i,self.__mots[i.lower()].nombre))

    def __init__(self,text:str):
        self.__texte=text
        self.traitement_text()

    def get_nombre_repet(self,mot:str):
        return self.__mots[mot.lower()].nombre

    def __nettoyage(self,m:str)->str:
        tmp = ""
        for i in m:
            if i not in self.__caractaire_speciaux:
                tmp += i
        return tmp

    def affichage_des_mot(self):
        for i in self.__mots:
            print(i)

    def retourne_mot(self,m:str)->Mot:
        return self.__mots[ m.lower() ]