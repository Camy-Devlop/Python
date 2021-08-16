class Produit:

    def __init__(self,marque:str,nom,prix):
        """
        :param str marque: la marque de qui prduit cette article
        :param str nom: nom de l'article
        :param prix float: le prix du produit
        """
        assert type(marque)==str,"nest pas un string "
        assert type(nom) == str, "nest pas un string "
        assert type(prix) == float, "nest pas un float "

        self.marque=marque
        self.nom=nom
        self.prix=prix
