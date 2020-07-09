class Calcule_ACGT():

    def compter_ACGT(self)->int:
        i=0
        while self.chaine[i]!='#':

            if self.chaine[i]=='A':
                self.Anb+=1
            elif self.chaine[i]=='C':
                self.Cnb+=1
            elif self.chaine[i]=='G':
                self.Gnb+=1
            elif self.chaine[i]=='T':
                self.Tnb+=1
            
            self.total_ACGT+=1
            i+=1
        
    def affichage_total(self):
        print("nombre d\'adénine A:",self.Anb)
        print("nombre de cytosine C:",self.Cnb)
        print("nombre de guanine G:",self.Gnb)
        print("nombre de thymine T:",self.Tnb)
        print("nombre de nucléotides:",self.total_ACGT)
    
    def __init__(self, chaine:str):
        self.chaine=chaine+'#'
        self.Anb=0
        self.Cnb=0
        self.Gnb=0
        self.Tnb=0
        self.total_ACGT=0


        