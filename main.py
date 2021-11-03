# ZADANIE1

def Zadanie1(name: str, surname: str) -> str:
    return "Cześć " + name + " " + surname


x = Zadanie1("Jan", "Kowalski")

print(x)


# ZADANIE2

def Zadanie2(x: int, y: int) -> int:
    return x * y


print(Zadanie2(4, 2))


# ZADANIE 3

def Zadanie3(x: int) -> bool:
    if x % 2 == 0:
        return 1
    else:
        return 0


wynik = Zadanie3(10)

if wynik == 1:
    print("Liczba parzysta")
elif wynik == 0:
    print("Liczba nieparzysta")


# ZADANIE4

def Zadanie4(x: int, y: int, z: int) -> bool:
    if x + y >= z:
        return 1
    else:
        return 0


print(Zadanie4(1, 1, 3))
print(Zadanie4(1, 2, 3))


# ZADANIE 5

def Zadanie5(x: list, y: int):
    for i in x:
        if i == y:
            return "Zawiera"

    return "Nie zawiera"


print(Zadanie5([1, 2, 4, 5], 5))


print(Zadanie5([1, 2, 4], 5))

# ZADANIE 6


def Zadanie6(x: list, y: list) -> list:
    z = x+y
    z = list(dict.fromkeys(z))
    i = 0
    for x in z:
        z[i] = x ** 3
        i += 1
    return z


print(Zadanie6([2, 3, 4, 5], [2, 3, 4]))
