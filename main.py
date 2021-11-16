import Zadanie1 as z1
import Zadanie2 as z2
import Zadanie3 as z3

Student1 = z1.Student("Paweł", 20)

Student2 = z1.Student("Piotr", 99)
print(Student1.is_passed())
print(Student2.is_passed())

Biblioteka1 = z2.Library("Katowice", "Kościuszki", "40-523", "8-22", "512623123")

Biblioteka2 = z2.Library("Rybnik", "3 Maja", "44-200", "10-19", "965852145")

Ksiazka1 = z2.Book(Biblioteka1, 1834, "Adam", "Mickiewicz", 400)
Ksiazka2 = z2.Book(Biblioteka1, 1889, "Bolesław", "Prus", 676)
Ksiazka3 = z2.Book(Biblioteka1, 1901, "Stanisław", "Wyspiański", 210)
Ksiazka4 = z2.Book(Biblioteka2, 1937, "Witold", "Gombrowicz", 295)
Ksiazka5 = z2.Book(Biblioteka2, 1943, "Aleksander", "Kamiński", 256)

Pracownik1 = z2.Employee("Jan", "Kowalski", "15/03/2016", "23/02/1991",
                         "Katowice", "Plebiscytowa", "40-525", "445889625")
Pracownik2 = z2.Employee("Robert", "Nowak", "24/06/2017", "12/08/1987",
                         "Katowice", "Środkowa", "40-525", "663558954")
Pracownik3 = z2.Employee("Piotr", "Polak", "01/12/2015", "17/05/1979",
                         "Rybnik", "Wodzisławska", "40-200", "636524151")

Zamowienie1 = z2.Order(Pracownik1, Student2, Ksiazka2, "22/03/2019")
Zamowienie2 = z2.Order(Pracownik3, Student1, Ksiazka5, "12/09/2021")

print(Zamowienie1)
print(Zamowienie2)

Dom1 = z3.House(150, 4, 300000, "Gotartowice ul. Zwierzyńska 41a", 170)

Dom2 = z3.Flat(120, 3, 200000, "Katowice ul.Budownicza 31", 1)

print(Dom1)
print(Dom2)
