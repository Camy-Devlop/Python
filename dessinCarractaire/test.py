import aiohttp.abc


def calcule(vitesse,distance,temps,h=3600,d=1000)->bool:
    t: [float] = list()
    t.append(vitesse) # la vitesse en Km/h
    t.append(distance/d) # la distance en Km :distance
    t.append(temps/h) #le temps en heure : h
    temps_calculer=t[1]/t[0]
    if temps_calculer*h<=temps:
        return True
    else:
        return False

def verification(a,b,c):
    v=a
    while (test:=calcule(a,b,c))!=True and a>0:
        a -= 0.100000
        a = int(a * 10)
        a = a / 10
        if a==1 and test==False:
            c+=c
            if (test:=calcule(((b/1000)/(c/3600)),b,c))==True:
                if v>=((b/1000)/(c/3600)):
                    a=((b/1000)/(c/3600))
                else:a=v
            else:a=v
    return test,a


print(verification(90 ,300 ,30))
#print(verification(50,200,30))

print((300/1000)/(30/3600))
print((1500/1000)/(20/3600))
print((3000/1000)/(10/3600))