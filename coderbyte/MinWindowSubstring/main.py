def MinWindowSubstring(strArr):
    class Mot:
        def __init__(self, mots:list):
            self._N = mots[0]
            self._K =mots[1]
            self._debut: int = 0
            self._fin: int = 0
            self.recherche()

        def __str__(self):
            if self._fin>0:
                if self.verif_tous(self._N[self._debut:self._fin],self._K):
                    return self._N[self._debut:self._fin]
                else:return ""
            else : return ""

        def verif_tous(self, mot, lettres: str) -> bool:
            cpt:list =list()
            cpt_chr_SetDico: set = set()
            cpt_chr_Dico: dict = {}
            for i in lettres:
                cpt_chr_SetDico.add((i, lettres.count(i)))

            for i in cpt_chr_SetDico:
                cpt_chr_Dico[i[0]] = i[1]
                if mot.count(i[0]) >= i[1]:
                    cpt=True
                else:
                    cpt=False
                    break
            return cpt


        def recherche(self):
            min=len(self._K)
            max=len(self._N)
            cpt = 0
            test =False
            while cpt < max and test == False:
                for i in range(max - (min - 1 + cpt)):
                    print(self._N[i:i + (min + cpt)],self.verif_tous(self._N[i:i + (min + cpt)],self._K))
                    self._debut=i
                    self._fin=i + min + cpt
                    test =self.verif_tous(self._N[i:i + min + cpt],self._K)
                    if test==True:
                        break
                cpt+=1
    return Mot(strArr)

#print(MinWindowSubstring(["ahffaksfajeeubsne", "aksfaje"]))
print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))
#print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))
#print(MinWindowSubstring(["aaffhkksemckelloe", "fhea"]))
#affhkkse

#aksfaje
