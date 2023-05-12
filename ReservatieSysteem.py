from Gebruikers import Gebruikers, Gebruiker
from Films import Films, Film
from Zalen import Zalen, Zaal
from Vertoningen import Vertoningen, Vertoning
from Reservaties import Reservaties, Reservatie

class ReservatieSysteem:

    def __init__(self):
        self.gebruikers = Gebruikers #Gebruikers container
        self.films = Films
        self.zalen = Zalen
        self.vertoningen = Vertoningen
        self.reservaties = Reservaties
    
    def nieuwe_gebruiker(self, voornaam, achternaam, email):
        return self.gebruikers.nieuwe_gebruiker(voornaam, achternaam, email)
    
    def nieuwe_film(self, titel, rating):
        return self.films.nieuwe_film(titel, rating)
    
    def nieuwe_vertoning(self, zaalnummer, slot, datum, filmid, vrije_plaatsen):
        return self.vertoningen.nieuwe_vertoning(zaalnummer, slot, datum, filmid, vrije_plaatsen)
    
    def nieuwe_zaal(self, zaalnummer, aantal_plaatsen):
        self.vertoningen.nieuwe_mogelijke_zaal(zaalnummer)
        return self.zalen.nieuwe_zaal(zaalnummer, aantal_plaatsen)
    
    def nieuwe_reservatie(self, userid, timestamp, vertoningid, aantal_plaatsen):
        return self.reservaties.nieuwe_reservatie(userid, timestamp, vertoningid, aantal_plaatsen)