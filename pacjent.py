class Pacjent:

    def __init__(self, imie: str, nazwisko: str, data_urodzenia: str, telefon: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia
        self.telefon = telefon

    @property
    def _imie(self):
        return self.imie

    @property
    def _nazwisko(self):
        return self.nazwisko

    @property
    def _data_urodzenia(self):
        return self.data_urodzenia

    @property
    def _telefon(self):
        return self.telefon

    def __str__(self):
        return f'Imię: {self.imie}, nazwisko: {self.nazwisko},' \
               f' data urodzenia: {self.data_urodzenia},' \
               f' telefon kontaktowy: {self.telefon}'
