#ADT Films
class Films:
    def __init__(self):
        self.container = [] #Container voor alle Films

    def nieuwe_film(self, titel, rating):
        """
        Maakt nieuwe film aan en voegt die toe aan films container

        preconditie : 
            (x) er bestaat nog geen Film met param:titel in de Films datastructuur

        postconditie : 
            (x) de nieuwe Film zit in de Films datastructuur 

        : param titel: type string
        : param rating : type float

        : return : succes bool

        """
        pass

#ADT Film

class Film(Films):
    #Data
    ID = 0 #wordt gebruikt om aan elke film een unieke id te geven, +1 bij elke Film init

    def __init__(self, titel, rating):
        """
        Film constructor, maakt nieuwe Film aan

        preconditie : 
            (x) titel is van type string, rating is van titel float
            (x) param:rating <= 10, param:rating >= 0
            (x) er bestaat nog geen Film met param:titel in de Films datastructuur


        postconditie : 
            (x) ID is met 1 verhoogt
            (x) er is een nieuwe Film aangemaakt met id, titel en rating

        : param titel: type string
        : param rating : type float

        : return : /

        """
        pass