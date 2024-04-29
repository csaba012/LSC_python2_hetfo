import random

# legyen 15 jegy infóból
jegyek = tuple(random.randint(1, 5) for i in range(15))

#a jegyek atlaga
#átlag = összeg / jegyek szama
atlag = sum(jegyek) / len(jegyek)

print(jegyek)
print(atlag)

# kupac amiben az első szám az egyesek száma
# a második a kettesek, harmadik a hármasok
# negyedik a négyesek, ötödik az ötösok száma
# (3, 5, 1, 2, 4)
lista = [0, 0, 0, 0, 0]
for elem in jegyek:
    lista[elem - 1] += 1
print(tuple(lista))

lista = []
for jegy in range(1, 6):
    lista.append(jegyek.count(jegy))
print(tuple(lista))

kupac = (
    jegyek.count(1), 
    jegyek.count(2), 
    jegyek.count(3), 
    jegyek.count(4), 
    jegyek.count(5)
)
print(kupac)

kupac = (
    (6, 7),
    (2, 3),
    (7, 6),
    (9, 8),
    (10, 2),
    (8, 9)
)
# szimmetrikus kupacokat egy másik listába ki kell gyűjteni
# [(6, 7), (7, 6), (9, 8), (8, 9)]
# forditott = konkret_kupac[::-1]
lista = []
for par in kupac:
    forditott = par[::-1]
    if forditott not in lista:
        if forditott in kupac:
            lista.append(par)
            lista.append(forditott)
print(lista)

kupac = (
    (3, 4),
    (78, 76), 
    (2, 3),
    (9, 8),
    (19, 23)
)

keresett = (17, 23)
# keressük azt a két elemű kupacot ami a legközelebb van a keresett kupachoz
elteres = (
    keresett[0] - kupac[0][0],
    keresett[1] - kupac[0][1]
)
index = 0
for i in range(1, len(kupac)):
    seged = (
        keresett[0] - kupac[i][0],
        keresett[1] - kupac[i][1]
    )
    if abs(elteres[0]) + abs(elteres[1]) > abs(seged[0]) + abs(seged[1]):
        elteres = seged
        index = i
print(kupac)
print(f"Keresett: {keresett}")
print(f"Legközelebbi: {kupac[index]}")

# kupac1 = 5db random szám 1-10ig
# kupac2 = 5db random szám 1-10ig
# a kérdés: kupac1 és kupac2 ugyan azokat az elemeket tartalmazzák-e?
kupac1 = tuple(random.randint(1, 10) for i in range(5))
kupac2 = tuple(random.randint(1, 10) for i in range(5))
print(kupac1)
print(kupac2)
if sorted(kupac1) == sorted(kupac2):
    print("Egyeznek az elemek")
else:
    print("Nem egyeznek az elemek")

kupac = tuple(random.randint(1, 50) for i in range(15))
# (1, 23, 40, 10, 9, 2, 3,...)
# mennyi a legkisebb különbség
# melyik két index-en érhető ez el
min_elteres =abs(kupac[1] - kupac[0])
index = 0
for i in range(1, len(kupac) - 1):
    if min_elteres > abs(kupac[i + 1] - kupac[i]):
        min_elteres = abs(kupac[i + 1] - kupac[i])
        index = i
print(kupac)
print(kupac[i], kupac[i + 1])
print(min_elteres)

