from dietetyk import Dietetyk as di


class Dieta(di):
    def __init__(self, imie: str, nazwisko: str, wiek: int, telefon: str, cena: float, kalorie: float):
        super().__init__(imie, nazwisko, wiek, telefon)
        self.cena = cena
        self.kalorie = kalorie

    @property
    def _cena(self):
        return self.cena

    @property
    def _kalorie(self):
        return self.kalorie

    def __str__(self):
        return f'Cena: {self.cena}, ilość kalorii: {self.kalorie},' \
               f' Imię autora diety: {self.imie},' \
               f' Nazwisko autora diety: {self.nazwisko}' \
               f' Wiek dietetyka: {self.wiek}' \
               f' Telefon do dietetyka: {self.telefon}\n'
