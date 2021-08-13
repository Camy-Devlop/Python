class Lettre:
    __cpt: int
    __lettre: chr

    def __init__(self, lettre: chr):
        self.__cpt = 1
        self.__lettre = str.lower(lettre)[0]

    def set_test(self, lettre: chr) -> bool:
        if self.__lettre == str(lettre).lower():
            self.__plus1
            return True
        else:
            return False

    @property
    def __plus1(self):
        self.__cpt += 1

    @property
    def get_cpt(self):
        return self.__cpt

    def __str__(self):
        return self.__lettre
