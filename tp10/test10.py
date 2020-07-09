
def factorel(n:int)-> int:
    k=1
    for i in range(1,n+1):
       k *=i

    return k

def arrangement_repit(n:int,k:int)->int:
    return int(factorel(n)/factorel(n-k))

#n = int(input())
#k=1
#if 0<=n and n<=100:
    a=1

print(arrangement_repit(10,2))