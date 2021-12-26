class SumSquareDifference:
    def __init__(self, a: int):

        assert a >= 0, "valeur négatif n'est pas Nombre nature "
        assert isinstance(a, int), "valeur a ne doit pas être un reel "

        self.res1: int = 0
        self.res2: int = 0
        for i in range(1, a + 1):
            self.res1 += int(float(i)**2)
            self.res2 += i

        self.res2 = self.res2**2
        self.total = self.res2 - self.res1
        print(self.total)

