#n = int(input())
#x = list(map(int,input().split()))
#while len(x) != 1:
#    x = [x[0]^x[1]]+x[2:]


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

#print(x[0])
p1= {0 : 9, 1 : 8, 2 : 7, 3 : 6, 4 : 5, 5 : 4, 6 : 3, 7 : 2}
p2 ={0 : 0, 1 : 8, 2 : 7, 3 : 6, 4 : 5, 5 : 4, 6 : 3, 7 : 2
1
8
Sortie
standard:
1
Informations:
Your
spaceship
targeted
mountain
1, your
altitude is now
8
BOOOOMM!! Nice
Shot!

Height
of
mountain
0: 0
Height
of
mountain
1: 0
Height
of
mountain
2: 7
Height
of
mountain
3: 6
Height
of
mountain
4: 5
Height
of
mountain
5: 4
Height
of
mountain
6: 3
Height
of
mountain
7: 2
2
8
Sortie
standard:
2
Informations:
Your
spaceship
targeted
mountain
2, your
altitude is now
7

Height
of
mountain
0: 0
Height
of
mountain
1: 0
Height
of
mountain
2: 0
Height
of
mountain
3: 6
Height
of
mountain
4: 5
Height
of
mountain
5: 4
Height
of
mountain
6: 3
Height
of
mountain
7: 2
3
8
Sortie
standard:
3
Informations:
Your
spaceship
targeted
mountain
3, your
altitude is now
6

Height
of
mountain
0: 0
Height
of
mountain
1: 0
Height
of
mountain
2: 0
Height
of
mountain
3: 0
Height
of
mountain
4: 5
Height
of
mountain
5: 4
Height
of
mountain
6: 3
Height
of
mountain
7: 2
4
8
Sortie
standard:
4
Informations:
Your
spaceship
targeted
mountain
4, your
altitude is now
5

Height
of
mountain
0: 0
Height
of
mountain
1: 0
Height
of
mountain
2: 0
Height
of
mountain
3: 0
Height
of
mountain
4: 0
Height
of
mountain
5: 4
Height
of
mountain
6: 3
Height
of
mountain
7: 2
5
8
Sortie
standard:
5
Informations:
Your
spaceship
targeted
mountain
5, your
altitude is now
4

Height
of
mountain
0: 0
Height
of
mountain
1: 0
Height
of
mountain
2: 0
Height
of
mountain
3: 0
Height
of
mountain
4: 0
Height
of
mountain
5: 0
Height
of
mountain
6: 3
Height
of
mountain
7: 2
6
8
Sortie
standard:
6
Informations:
Your
spaceship
targeted
mountain
6, your
altitude is now
3

Height
of
mountain
0: 0
Height
of
mountain
1: 0
Height
of
mountain
2: 0
Height
of
mountain
3: 0
Height
of
mountain
4: 0
Height
of
mountain
5: 0
Height
of
mountain
6: 0
Height
of
mountain
7: 2
7
8
Sortie
standard:
7
Informations:
Congratulations, you
can
land
with your spaceship!

Height
of
mountain
0: 0
Height
of
mountain
1: 0
Height
of
mountain
2: 0
Height
of
mountain
3: 0
Height
of
mountain
4: 0
Height
of
mountain
5: 0
Height
of
mountain
6: 0
Height
of
mountain
7: 0



while True:
    d = 9
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        # The index of the mountain to fire on.
        if 0 <= mountain_h and mountain_h <= 9:
            m[i] = p[mountain_h] = True
            print(i)
            d -= 1

