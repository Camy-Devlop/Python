n = int(input())
m = int(input())
p = []
for i in range(max(2,n),max(2,m+1)):
    print(i)
    f=True
    for j in range(2,i):
        if i%j==0:f=False
    if f:p.append(i)
if p:print(*p)
else:print(-1)