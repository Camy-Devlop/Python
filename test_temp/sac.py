class Sac:
    def __init__(self):
        self.end = 0
        if self.end < 0:
            raise ValueError("Point d'arret de l'interval invalide")
        self.liste = []
        self.cpt = 0

    def add(self, item):
        self.liste.append(item)
        self.end += 1

    def __iter__(self):
        return iter(self.liste)

    def __next__(self):
        return next(self.liste)
