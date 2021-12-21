class Dietetyk:

    def __init__(self, imie: str, nazwisko: str, wiek: int, telefon: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.telefon = telefon

    @property
    def _imie(self):
        return self.imie

    @property
    def _nazwisko(self):
        return self.nazwisko

    @property
    def _wiek(self):
        return self.wiek

    @property
    def _telefon(self):
        return self.telefon

    def __str__(self):
        return f'Imię: {self.imie}, nazwisko: {self.nazwisko},' \
               f' wiek: {self.wiek},' \
               f' telefon kontaktowy: {self.telefon}'
