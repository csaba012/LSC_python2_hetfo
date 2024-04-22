import random

ures_kupac = ()
kuapc1 = (1, 2, 3, 4)
kuapc2 = (1, "logiscool", True, [1, 2, 3], kuapc1)
print(kuapc2)
kuapc3 = (1,)
print(type(kuapc3))
kuapc4 = 1, 2, 3, 
print(type(kuapc4))

lista = [1, 2, 3]
kuapc5 = (1, 2, 3)
lista.append(4)
print(lista)

kupac = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(kupac[3])
print(kupac[2:5])
print(kupac[-1])
print(len(kupac))

kupac6 = (1, 2, 3)
kupac7 = (4, 5, 6)
print(kupac6 == kupac7)

kupac6 = (3, 4, 5)
kupac7 = (5, 4, 3)
print(kupac6 == kupac7)

kupac6 = (1, 2, 3)
kupac7 = (1, 2, 3)
print(kupac6 == kupac7)
print(kupac6 == (1, 2, 3))

print(kupac6, kupac7)
print(kupac6 + kupac7)
print(kupac6 * 3)

kupac = (1, 2, 3, 4, 5, 6)
kupac_lista = list(kupac)
print(type(kupac_lista))
kupac_lista.append(7)
kupac_lista.insert(0, -1)
del kupac_lista[2]
kupac = tuple(kupac_lista)
print(kupac)
print(type(kupac))

# létre kell hozni egy 10 elemű, random számokból álló kupacot 
# (1, 20 közötti random számok)
# ki kell írni a kupacot
# a páros elemeket írja ki
random_kupac = tuple(random.randint(1, 20) for i in range(10))
print(random_kupac)
for elem in random_kupac:
    if elem % 2 == 0:
        print(elem)

kupac = (1, 2, 3, 4, 5, 2, 1, 4, 2, 4, 5)
print(2 in kupac)
print(kupac.count(2))
print(kupac.index(2))

kupac = (1, 2, 3)
a, b, c = kupac
print(a)
print(b)
print(c)

kupac = ((1, 2, 3), (4, 5, 6), (10, 20, 60, 40), (-1, -5, -7))
#végeredményben egy kupacot szeretnék, aminek az elemei
# az egyes kupacok átlaga
# (2.0, 5.0, 32.5, -4.3333333333)
atlag_lista = []
for elem in kupac:
    atlag = sum(elem) / len(elem)
    atlag_lista.append(atlag)
atlag_kupac = tuple(atlag_lista)
print(atlag_kupac)

print(tuple(sum(i) / len(i) for i in kupac))

#kupac = (1, 2, 3, 4)
#kupac[2] = -1
#print(kupac)

kupac = (0, 0, 0, 0)
kupac = kupac[:2] + (1,) + kupac[2:]
print(kupac)