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
