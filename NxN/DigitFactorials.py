from math import factorial
class DigitFactorials:
    def __init__(self, a: str):
        self.res=0
        for i in a:
            self.res+=factorial(int(i))
        print(self.res)