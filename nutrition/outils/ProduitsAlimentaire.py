class ProduitAlimentaire:
    def __init__(self, nom: str, cal_100g: float, masse: float):
        self.__nom_produit: str = nom
        self.__gr_100: float = cal_100g
        self.masse: float = masse

    @property
    def kj_total(self)-> float: return self.masse/self.__gr_100

    @property
    def cal_total(self) -> float: return self.masse / self.__gr_100
