#ADT Gebruiker
class Gebruikers:
    
    def __init__(self):
        self.container = [] #Container voor alle gebruikers

    def nieuwe_gebruiker(self, voornaam ,achternaam , email):
        """
        Maakt nieuwe Gebruiker aan en voegt die toe aan de Gebruikers container

        precondities : 
            (x) er bestaat nog geen Gebruiker met voornaam param:voornaam en achternaam
                param:achternaam

        postcondities : 
            (x) de nieuwe Gebruiker zit in de Gerbuikers datastructuur 

        : param voornaam : type string
        : param achternaam : type string
        : param email: type string

        : return : succes bool

        """
        pass
        

class Gebruiker(Gebruikers):
    #Data
    ID = 0 #wordt gebruikt om aan elke Gebruiker een unieke id te geven, +1 bij elke Gebruiker init

    def __init__(self, voornaam, achternaam, email):
        """
        Gebruiker constructor, maakt nieuwe Gebruiker aan

        precondities : 
            (x) de check_email methode returnt True

        postcondities : 
            (x) ID is met 1 verhoogt
            (x) de nieuwe Gebruiker bevat een id, voornaam, achternaam, email

        : param voornaam : type string
        : param achternaam : type string
        : param email: type string

        : return : /

        """
        pass