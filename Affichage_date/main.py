from affichage import Affichage
import decodage_str
from calcule import *
from CONFIGS import *
#dates = decodage_str.demander_infos()
#a=Affichage()
#a.affichage(dates[0],dates[1])
from calendrie import Calandrie

a=Calandrie(31)
#a.EEE()

for v in a:
    print(a.jour_semain_str(v.value_int))