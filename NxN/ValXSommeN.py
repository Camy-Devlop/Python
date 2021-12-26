class ValXSommeN:

    def __init__(self, val: int, expo: float):
        assert isinstance(val, int), "TypeError can only concatenate int (not str) to int"

        self.val = val
        self.expo = expo
        self.val_str = str(val**expo)
        print("mon test", self.val_str)

    def string_somme(self):
        res = 0
        self.val_str = self.val_str.replace(".", "", 1)

        for i in self.val_str:
            res += int(i)
        return res.__str__()

    def string_prod(self):
        res = 0
        print("avant ", self.val_str)
        val_str = self.val_str.replace(".", "", 1)
        val_str = val_str.replace("0", "")
        for i in val_str:
            res += int(i)
        print(val_str)
        return res.__str__()
