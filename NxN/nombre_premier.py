class NbPremier:

    def __init__(self, nb: int):
        self.tab_nb_int = [2]
        for i in range(2, nb+1):
            if i % 2 != 0:
                if multiple(i):
                    if i not in self.tab_nb_int:
                        self.tab_nb_int.append(i)

    def somme_premier(self) -> int:
        res = 0
        for i in self.tab_nb_int:
            res += i
        return res

    def prod_premier(self) -> int:
        res = 1
        for i in self.tab_nb_int:
            res *= i
        return res


def multiple(a: int) -> bool:
    for i in range(3, int(a**0.5)+1, 2):
        if a % i == 0:
            return False

    return True
