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
else:print(-1

c = int(input())
_list = input()
liste = []
for i in _list.split():
    liste.append(i.lower())
n = int(input())
for i in range(n):
    res = ""
report = input()
for j in report.split():
    if
j.lower() not in liste:
res += j + " "
else:
res += j[0] + (len(j) - 2) * "*" + j[-1] + " "
print(res[:-1])
