
def verifie_ischiffre(entre)->bool:
    cpt:int=0
    for x in list(str(entre)):
        if x in "0123456789":
            pass
        else:
            cpt+=1


    if cpt>0:
        return False
    else:
        return True
