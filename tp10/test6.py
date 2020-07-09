n = input()
l = [int(i) for i in n]

tmp = float("inf")
for i in l:
    if i != tmp :
        tmp = i
        print(i, end="")
print("")