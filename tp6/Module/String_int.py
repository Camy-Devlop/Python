

class String_int():

    def __init__(self,_2char:str,val:int):
        self.part1:str=_2char
        self.part2:int=val


    def __str__(self):
        if len(str(self.part2))==2:
            return self.part1+str(self.part2)

        elif len(str(self.part2))==1:
            return self.part1 + (str(self.part2)).zfill(2)

        elif len(str(self.part2))>2:
            return None

        else:
            return None

