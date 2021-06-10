class Calcule_ACGT():

    def compter_ACGT(self):
        self.Anb=self.chaine.count(self.GROUP_ATCG[0])
        self.Tnb=self.chaine.count(self.GROUP_ATCG[1])
        self.Cnb+=self.chaine.count(self.GROUP_ATCG[2])
        self.Gnb=self.chaine.count(self.GROUP_ATCG[3])
        self.total_ACGT+=self.Anb+self.Tnb+self.Cnb+self.Gnb

    def compte_AT_GC(self)->(float,float):
        """
            il va compter le nombre de AT et GC dans la chaine d'ADN

        :return: il va remetre les deux valeur en pourcent
        la premier valeur c'est AT et la deuxieme c'est GC
        """
        return (((self.Gnb+self.Cnb)/self.total_ACGT),(self.Anb+self.Tnb)/self.total_ACGT)

    def affichage_total(self):
        print("nombre d\'adénine A:",self.Anb)
        print("nombre de cytosine C:",self.Cnb)
        print("nombre de guanine G:",self.Gnb)
        print("nombre de thymine T:",self.Tnb)
        print("nombre d\'adénine A:", self.Anb)
        print("nombre de cytosine AT:", self.ATnb)
        print("nombre de cytosine GC:", self.GCnb)
        print("nombre de nucléotides:",self.total_ACGT)
    
    def __init__(self, chaine:str):
        self.GROUP_ATCG="ATCG"
        self.chaine=chaine+'#'
        self.Anb=0
        self.Cnb=0
        self.Gnb=0
        self.Tnb=0
        self.ATnb=0
        self.GCnb=0
        self.total_ACGT=0

        """ def compte_AT_et_GC(self)->(float,float):

                    il va compter le nombre de AT et GC dans la chaine d'ADN

                :return: il va remetre les deux valeur en pourcent
                la premier valeur c'est AT et la deuxieme c'est GC

                i = 0
                while self.chaine[i] != '#':
                    if self.chaine[i:i+2] == 'AT':
                       self.ATnb +=1

                    elif self.chaine[i:i+2] == 'GC':
                        self.GCnb+=1

                    i += 1
                #print(((self.ATnb/(self.ATnb+self.GCnb)),(self.GCnb/(self.ATnb+self.GCnb))))
                return ((self.GCnb/(self.ATnb+self.GCnb)),self.ATnb/(self.ATnb+self.GCnb))
        """