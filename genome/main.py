from calcule.calcule_ACGT import Calcule_ACGT as ADN
from calcule.repetition import Repetition as rep
from calcule.codon import Codon
import re

#aa="AACTCTATATTTTATTTTTGGAATTTGAGCAGGTTTAGTTGGAACTTCATTAAGTCTTCTAATTCGTACTGAATTAGGTACCCCAGGATCTTTAATTGGAGACGACCAAATTTATAATACTATTGTAACAGCTCATGCATTTATTATAATTTTTTTCATAGTAATACCTATTATAATTGGAGGATTTGGAAATTGATTAGTACCCTTAATATTAGGAGCTCCAGATATAGCATTTCCTCGAATAAATAATATAAGATTTTGATTATTACCCCCATCCTTGACCCTATTAATTTCAAGAAGTATTGTAGAAAATGGTGCTGGTACTGGTTGAACTGTATATCCCCCACTTTCATCTAATATTGCCCACCAAGGAGCTTCTGTTGACTTAGCAATTTTTTCCCTTCATCTTGCAGGTATTTCTTCTATTTTAGGAGCTATTAATTTTATTACAACTATTATTAATATACGAATTAATAATATATCATTTGATCAAATACCATTATTTGTTTGAGCAGTAGGAATTACTGCTTTATTATTATTACTTTCTTTACCAGTTTTAGCTGGTGCTATTACTATATTATTAACAGACCGAAATCTTAATACTTCATTTTTTGATCCTGCTGGAGGAGGTGATCCTATTTTATACCAACATTTATTT"
aa="CCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAA"
#aa="TTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGG"
a=ADN(aa)
b=Codon(aa)
b.affiche_list_adn_codon()
print("-----------------------------------------------------")



"""
mystr = 'Bonbonbonbonbon'

pattern = r'((.{3}).*({}))'
for iiii in range(int(len(mystr)/3)):
    match = re.search(pattern, mystr)

results = match.groups() # ('foo1', 'foo2 foo3 (foo4)')



print(results)
"""
#r.couper()
#r.affichage_N(15)
#r.nombre_repeter(15)


