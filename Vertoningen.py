#ADT Vertoningen
class Vertoningen:
    def __init__(self):
        self.container = []
        self.mogelijke_zalen = []

    def nieuwe_vertoning(self, zaalnummer, slot, datum, filmid, vrije_plaatsen):
        """
        Maakt nieuwe Vertoning en zet die in de Vertoningen container

        preconditie : 
            (x) er bestaat nog geen vertoning met param:zaalnummer, param:slot, param:datum en param:filmid 


        postconditie : 
            (x) de nieuwe Vertoning zit in de Vertoningen datastructuur 

        : param zaalnummer : type int
        : param slot : Tijd object (-> /src/TimeStamp.py Tijd object)
        : param datum: Datum object (-> /src/TimeStamp.py Datum object)
        : param filmid : type int
        : param vrije_plaatsen : type int

        : return : succes bool

        """
        pass
    def nieuwe_mogelijke_zaal(self, zaalnummer):
        """
        Voegt zaalnummer toe aan mogelijke zalen

        precondities: /

        postcondities: 
            (x) Voegt param:zaalnummer toe aan mogelijke_zalen als het er nog niet in zat
        """

#ADT Vertoning

class Vertoning:
    #Data
    ID = 0 #wordt gebruikt om aan elke Vertoning een unieke id te geven, +1 bij elke Vertoning init

    def __init__(self, zaalnummer, slot, datum, filmid, vrije_plaatsen):
        """
        Vertoning constructor, maakt nieuwe Vertoning aan

        preconditie : 
            (x) er bestaat een Zaal met param:zaalnummer
            (x) er bestaat een Film met param:filmid
            (x) param:slot is een Tijd object en zit in de lijst van toegestane tijdsslots (-> Vertoningen.slots)
            (x) param:datum is een Datum object 
            (x) param:vrije_plaatsen is strikt kleiner dan het aantal vrije plaatsen
                in Zaal met param:zaalnummer


        postconditie : 
            (x) ID is met 1 verhoogt
            (x) er is een nieuwe Vertoning aangemaakt met ID, zaalnummer, slot, datum, filmid, vrije_plaatsen

        : param zaalnummer : type int
        : param slot : Tijd object (-> /src/TimeStamp.py Tijd object)
        : param datum: Datum object (-> /src/TimeStamp.py Datum object)
        : param filmid : type int
        : param vrije_plaatsen : type int

        : return : succes bool

        """
        pass