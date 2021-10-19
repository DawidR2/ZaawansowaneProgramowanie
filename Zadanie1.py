lista_imion=['Arek', 'Marek', 'Paweł', 'Piotr', 'Michał']
lista_liczb=[1, 2, 3, 4, 5]
lista_liczb3=[1, 2, 3, 4, 5]

def wyswietl(imiona):
    for x in imiona:
        print(x)

def oblicz(liczby):
    i=0
    for x in liczby:
        liczby[i]=x*2
        i+=1
    return liczby

def oblicz2(liczby):
    wynik = [x*2 for x in liczby]

    return wynik


print("ZADANIE A")
wyswietl(lista_imion)
print("ZADANIE Bi")
print(oblicz(lista_liczb))
print("ZADANIE Bii")
print(oblicz2(lista_liczb3))

lista_liczb2=[1, 24, 31, 12, 15, 95, 23, 65, 83, 81]
print("ZADANIE C")
for x in lista_liczb2:
    if x%2==0:
        print(x)
print("ZADANIE D")
i=0
for x in lista_liczb2:
    i=i+1
    if i%2==0:
        print(x)
