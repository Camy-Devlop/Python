l = int(input())
h = int(input())
t = input()
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
dc={}
#row c'est le desin de chaque caractaire en fonction de la longeur : l et la hauteur : H
# la chaine de caractaire a dessiner : t
for i in alpha:
    dc[i]=[]

for i in range(h):
    cpt=0
    row = input()
    for j in range(0,len(row),l):
        dc[alpha[cpt]].append(row[j:j+l])
        cpt+=1

lettre_espace=[]
for i in range(h):
    lettre_espace.append(" "*l)
dc[" "]=lettre_espace
r=[]

for i in t.upper():
    if i in alpha:
        r.append(dc[i])
    else:
        r.append(dc["?"])

final=""
for i in range(h):
    for j in range(len(r)):
        final+=r[j][i]
    final+="\n"

print(final)