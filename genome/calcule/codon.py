from Fichier.recupe_List_codon import Fichier_codon


class Codon:

    def tab_codon(self,):
        pass

    def __init__(self, adn:str):
        self.adn=adn
        self.liste_codon_ref=(Fichier_codon()).get_liste_codon()
        self.liste_codon_ref2=self.liste_codon_ref
        self.tab_adn_codon=[]
        self.separateur_codon()

    def separateur_codon(self):
        t=""
        cpt=1
        for ss in self.adn:
            t += ss
            if cpt == 3:
                self.tab_adn_codon.append(t)
                t = ""
                cpt = 0
            cpt += 1
        self.tab_adn_codon.append(t)

    def affiche_l(self):
        for l in self.liste_codon_ref:
            print(l)

    def affiche_list_adn_codon(self):
        for l in self.tab_adn_codon:
            print(l)