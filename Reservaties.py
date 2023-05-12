#ADT Reservaties
class Reservaties:
    def __init__(self):
        self.container = []

    def nieuwe_reservatie(self, userid, timestamp, vertoningid, aantal_plaatsen):
        """
        Maakt niewe reservatie en plaatst die in de Reservaties container

        precondities: 
            (x) er bestaat een Gebruiker met id param:userid
            (x) er bestaat een vertoning met id param:vertoningid
            (x) param:timestamp zit in lijst van mogelijke timestamps
            (x) er bestaat nog geen reservatie met param:userid, param:timestamp, param:vertoningid
            (x) param:aantal_plaatsen is strikt kleiner of gelijk aan het aantal vrije
                plaatsen voor de Vertoning met id param:vertoningid 
            
        postcondities:
            (x) een nieuwe Reservatie is toegevoegd aan de container van Reservaties

        : param userid : type int
        : param timestamp : TimeStamp object (-> /src/TimeStamp.py)
        : param vertoningid : type int
        : param aantal_plaatsen : type int

        return: succes bool
        """
        pass

#ADT Reservatie

class Reservatie(Reservaties):
    #Data
    ID = 0 #wordt gebruikt om aan elke Reservatie een unieke id te geven, +1 bij elke Reservatie init

    def __init__(self, userid, timestamp, vertoningid, aantal_plaatsen):
        """
        Reservatie constructor, maakt een nieuwe Reservatie aan

        preconditie : 
            (x) param:timestamp is een Timestamp object (-> /src/TimeStamp.py)


        postconditie : 
            (x) ID is met 1 verhoogt
            (x) er is een nieuwe Reservatie aangemaakt met een ID, userid, timestamp, veroningid, aantal_plaatsen

        : param userid : type int
        : param timestamp : TimeStamp object (-> /src/TimeStamp.py)
        : param vertoningid : type int
        : param aantal_plaatsen : type int

        : return : /

        """
        pass