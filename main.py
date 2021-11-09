class Produkt:

    def __init__(self, nazwa: str, cena: float, kod_produktu: int, kod_kreskowy: int, kraj_pochodzenia: str):
        self.nazwa = nazwa
        self.cena = cena
        self.kod_produktu = kod_produktu
        self.kod_kreskowy = kod_kreskowy
        self.kraj_pochodzenia = kraj_pochodzenia

        @property
        def nazwa(self) -> None:
            return self.nazwa

        @property
        def cena(self) -> None:
            return self.cena

        @property
        def kod_produktu(self) -> None:
            return self.kod_produktu

        @property
        def kod_kreskowy(self) -> None:
            return self.kod_kreskowy

        @property
        def kraj_pochodzenia(self) -> None:
            return self.kraj_pochodzenia

    def __str__(self):
        print
        f'Nazwa produktu: {self.nazwa},' \
        f' cena produktu: {self.cena},' \
        f' kod produktu: {self.kod_produktu},' \
        f' kod kreskowy: {self.kod_kreskowy},' \
        f' kraj pochodzenia: {self.kraj_pochodzenia}  '


class Magazyn:

    def __init__(self, panstwo: str, miasto: str, ulica: str, numer_ulicy: int, telefon: str):
        self.panstwo = panstwo
        self.miasto = miasto
        self.ulica = ulica
        self.numer_ulicy = numer_ulicy
        self.telefon = telefon

        @property
        def panstwo(self) -> None:
            return self.panstwo

        @property
        def miasto(self) -> None:
            return self.miasto

        @property
        def ulica(self) -> None:
            return self.ulica

        @property
        def numer_ulicy(self) -> None:
            return self.numer_ulicy

        @property
        def telefon(self) -> None:
            return self.telefon

    def __str__(self):
        print
        f'Magazyn znadjudję się w: {self.panstwo},' \
        f' w mieście: {self.miasto},' \
        f' na ulicy: {self.ulica} {self.numer_ulicy}.' \
        f' Telefon kontaktowy: {self.telefon} '


class KlientDetaliczny:

    def __init__(self, imie: str, nazwisko: str, data_urodzenia: str, adres: str, telefon: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia
        self.adres = adres
        self.telefon = telefon

        @property
        def imie(self) -> None:
            return self.imie

        @property
        def nazwisko(self) -> None:
            return self.nazwisko

        @property
        def data_urodzenia(self) -> None:
            return self.data_urodzenia

        @property
        def adres(self) -> None:
            return self.adres

        @property
        def telefon(self) -> None:
            return self.telefon

    def __str__(self):
        print
        f'Imię: {self.imie}, nazwisko: {self.nazwisko},' \
        f' data urodzenia: {self.data_urodzenia},' \
        f' adres zamieszkania: {self.adres},' \
        f' telefon kontaktowy: {self.telefon}'


class KlientBiznesowy:

    def __init__(self, imie: str, nazwisko: str, data_urodzenia: str, nazwa_firmy: str, telefon: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia
        self.nazwa_firmy = nazwa_firmy
        self.telefon = telefon

        @property
        def imie(self) -> None:
            return self.imie

        @property
        def nazwisko(self) -> None:
            return self.nazwisko

        @property
        def data_urodzenia(self) -> None:
            return self.data_urodzenia

        @property
        def nazwa_firmy(self) -> None:
            return self.nazwa_firmy

        @property
        def telefon(self) -> None:
            return self.telefon

    def __str__(self):
        print
        f'Imię: {self.imie}, nazwisko: {self.nazwisko},' \
        f' data urodzenia: {self.data_urodzenia},' \
        f' nazwa firmy: {self.nazwa_firmy},' \
        f' telefon kontaktowy: {self.telefon}'


class Zamowienie(KlientBiznesowy, KlientDetaliczny, Magazyn, Produkt):

    def __init__(self):
        self.ilosc = None
        self.imie_klienta = None
        self.nazwisko_klienta = None
        self.produkt = None
        self.adres_klienta = None

        @property
        def imie_klienta(self) -> None:
            return self.imie_klienta

        @imie_klienta.setter
        def imie_klienta(self, value):
            self.imie_klienta = value

        @property
        def nazwisko_klienta(self) -> None:
            return self.nazwisko_klienta

        @nazwisko_klienta.setter
        def nazwisko_klienta(self, value):
            self.nazwisko_klienta = value

        @property
        def ilosc(self) -> None:
            return self.ilosc

        @ilosc.setter
        def ilosc(self, value):
            self.ilosc = value

        @property
        def produkt(self) -> None:
            return self.produkt

        @produkt.setter
        def produkt(self, value):
            self.produkt = value

        @property
        def adres_klienta(self) -> None:
            return self.adres_klienta

        @adres_klienta.setter
        def adres_klienta(self, value):
            self.adres_klienta = value




p = Produkt('Masło', 5, 120591, 19319519258, 'Polska')
m = Magazyn('Polska', 'Poznań', 'Kościuszki', 41, '902124512')
d = KlientDetaliczny('Jan', 'Kowalski', '23/04/1987', 'Rybnik, 1 maja 41', '09128395')
b = KlientBiznesowy('Paweł', 'Nowak', '13/08/1978', 'Katowice, plebiscytowa 21', '0987421284')

z = Zamowienie()
z.ilosc = 10
z.imie_klienta = d.imie
z.nazwisko_klienta = d.nazwisko
z.produkt = p
z.adres_klienta = d.adres

print(z)

