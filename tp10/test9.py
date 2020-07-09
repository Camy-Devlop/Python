from random import randint as rnd
def nombre_list_int(v,de=1,a=100)->list:

    return [rnd(de,a) for i in range(v)]

def test_croissant(n:int)->bool:

    nn=[int(i) for i in str(n)]
    tmp_list=sorted(nn)
    if nn==tmp_list:
        return {n:True}
    else:
        return {n:False}


print(test_croissant(nombre_list_int(1)[0]))