
class My_date:
    __jour:int
    __mois:int
    __anne:int
    def __init__(self,jour:int,mois:int,anne:int):
        self.__jour=jour
        self.__mois = mois
        self.__anne = anne
    def num2chr(self,a:int):
        if len(str(self.__jour)) < 2:
            return "0{0}".format(a)
        else:
            return str(self.__jour)

    @property
    def date(self)->str:
           return "{0}/{1}/{2}".format(self.num2chr(self.__jour),self.num2chr(self.__mois),self.__anne)

