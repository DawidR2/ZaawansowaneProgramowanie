import dieta as d
import dietetyk as di
import pacjent as p


class Zamowienie:
    @property
    def diety(self) -> list:
        return self.diety

    @diety.setter
    def diety(self, diety: list):
        self._diety = diety

    @property
    def dietetyk(self) -> di.Dietetyk:
        return self._dietetyk

    @dietetyk.setter
    def dietetyk(self, dietetyk: di.Dietetyk):
        self._dietetyk = dietetyk

    @property
    def pacjent(self) -> p.Pacjent:
        return self._pacjent

    @pacjent.setter
    def pacjent(self, pacjent: p.Pacjent):
        self._pacjent = pacjent

    def oblicz_kwote(self):
        cena = 0
        for d in self._diety:
            cena += d.cena
        return round(cena, 2)

    def ilosc_kalorii(self):
        kalorie = 0
        for d in self._diety:
            kalorie += d.kalorie
        return round(kalorie, 2)

    def __str__(self):
        return f'Pacjent: {self._pacjent}\n' \
               f'Dietetyk: {self._dietetyk}\n' \
               f"Diety:\n{''.join(str(x) for x in self._diety)}"


z = Zamowienie()

z.pacjent = p.Pacjent('Jan', 'Nowak', "21/04/93", "942345123")
z.dietetyk = di.Dietetyk('Robert', 'Nijaki', 54, "997623123")
z.diety = [d.Dieta('Robert', 'Nijaki', 54, "997623123", 120, 2500),
           d.Dieta('Robert', 'Nijaki', 54, "997623123", 400, 3000),
           d.Dieta('Robert', 'Nijaki', 54, "997623123", 300, 5000), ]

print(z)
print(z.ilosc_kalorii())
print(z.oblicz_kwote())
