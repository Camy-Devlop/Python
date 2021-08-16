from Sapin import Sapin

if __name__ == '__main__':
    #sapin=Sapin(5)
    m=[int,int,int]
    tab=list()
    tab.append(m)
    print(tab)
    for i in range(1,12):
        m=[i,0 if i<2 else i+i-1]
        print(f"{" {''*m[0]} {i}")

