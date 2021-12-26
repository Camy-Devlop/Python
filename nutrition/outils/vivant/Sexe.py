class Sexe:
    def __init__(self, sex: str):
        if sex == "homme" or sex == "femme":
            self.__sex: str = sex
        else:
            raise ValueError("les valeur attendu est homme ou femme")
    @property
    def sexe(self) -> str: return self.__sex

