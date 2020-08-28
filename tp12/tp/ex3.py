import collections

square = {2: 4, 3: 9, -1: 1, -2: 4}

# the largest key
key1 = max(square)
print("The largest key:", key1)    # 2
print(square)
p=collections.OrderedDict(sorted(square.items()))
di=dict()
pp=sorted(p)
for i in pp:
    di[i]=p[i]

print(di)