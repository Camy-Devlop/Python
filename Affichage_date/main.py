from affichage import Affichage
import decodage_str
from calcule import *
from CONFIGS import *
dates = decodage_str.demander_infos()
a=Affichage()
a.affichage(dates[0],dates[1])

