# ZADANIE 1
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'student: {self.name}'

    def is_passed(self) -> bool:
        if self.marks > 50:
            return bool(1)
        else:
            return bool(0)


Student1 = Student("Paweł", 20)


Student2 = Student("Piotr", 99)
print(Student1.is_passed())
print(Student2.is_passed())

# ZADANIE 2


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Miasto: {self.city}, ulica: {self.street},' \
               f' kod pocztowy: {self.zip_code}, godziny otwarcia:' \
               f' {self.open_hours}, telefon: {self.phone}'


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Zamówienie wydane przez {self.employee} dla {self.student}' \
               f' w postaci {self.books} dnia {self.order_date}'


class Employee:
    def __init__(self, first_name, last_name, hire_date,
                 birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'pracownik: Imię = {self.first_name},' \
               f' nazwisko = {self.last_name},' \
               f' data zatrudnienia = {self.hire_date},' \
               f' data urodzenia = {self.birth_date},' \
               f' miasto = {self.city}, ulica = {self.street},' \
               f' kod pocztowy = {self.zip_code},' \
               f' numer telefonu = {self.phone}'


class Book():
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surnname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'książki z biblioteki ({self.library}),' \
               f' data publikacji = {self.publication_date},' \
               f' imię autora = {self.author_name},' \
               f' nazwisko autora = {self.author_surnname},' \
               f' liczba stron = {self.number_of_pages}'


Biblioteka1 = Library("Katowice", "Kościuszki", "40-523", "8-22", "512623123")


Biblioteka2 = Library("Rybnik", "3 Maja", "44-200", "10-19", "965852145")

Ksiazka1 = Book(Biblioteka1, 1834, "Adam", "Mickiewicz", 400)
Ksiazka2 = Book(Biblioteka1, 1889, "Bolesław", "Prus", 676)
Ksiazka3 = Book(Biblioteka1, 1901, "Stanisław", "Wyspiański", 210)
Ksiazka4 = Book(Biblioteka2, 1937, "Witold", "Gombrowicz", 295)
Ksiazka5 = Book(Biblioteka2, 1943, "Aleksander", "Kamiński", 256)

Pracownik1 = Employee("Jan", "Kowalski", "15/03/2016", "23/02/1991",
                      "Katowice", "Plebiscytowa", "40-525", "445889625")
Pracownik2 = Employee("Robert", "Nowak", "24/06/2017", "12/08/1987",
                      "Katowice", "Środkowa", "40-525", "663558954")
Pracownik3 = Employee("Piotr", "Polak", "01/12/2015", "17/05/1979",
                      "Rybnik", "Wodzisławska", "40-200", "636524151")

Student3 = Student("Rafał", 66)

Zamowienie1 = Order(Pracownik1, Student2, Ksiazka2, "22/03/2019")
Zamowienie2 = Order(Pracownik3, Student1, Ksiazka5, "12/09/2021")

print(Zamowienie1)
print(Zamowienie2)

# ZADANIE 3


class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):

    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Powierzchnia domu:  {self.area}m²,' \
               f' ilość pokoi: {self.rooms},' \
               f' cena: {self.price}zł, adres: {self.address},' \
               f' powierzchnia działki: {self.plot}m² '


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Powierzchnia domu:  {self.area}m²,' \
               f' ilość pokoi: {self.rooms}, cena: {self.price}zł,' \
               f' adres: {self.address}, ilość pięter: {self.floor} '


Dom1 = House(150, 4, 300000, "Gotartowice ul. Zwierzyńska 41a", 170)


Dom2 = Flat(120, 3, 200000, "Katowice ul.Budownicza 31", 1)

print(Dom1)
print(Dom2)
