
class Fichier_codon:


    def recuperation(self):

        for ligne in self.fichier:
            self.list_codon.append((str(ligne).strip("\n")).split(','))
        # mmm[cpt]=mmm[cpt].strip("\n")

    def __init__(self):
        self.fichier = None
        self.list_codon = None

        try:
            self.fichier = open("Lib/codon.txt", "r")
            self.list_codon = []
            self.recuperation()

        except:
            print("Fichier Codon.txt n\'existe pas ")
        finally:
            self.fichier.close()



    def get_liste_codon(self)->list:

        return self.list_codon

    def affiche_list_codon(self):
        for l in self.list_codon:
            print(l)