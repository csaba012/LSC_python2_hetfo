import random
import matplotlib.pyplot as plt

def negyzetSzamok():
    szam = 1
    while True:
        yield szam * szam
        szam += 1

for elem in negyzetSzamok():
    if elem > 100:
        break
    print(elem)

szamok = []
for i in range(20):
    szam = random.randint(1, 100)
    if szam not in szamok:
        szamok.append(szam)
print(szamok)

def paros(lista):
    #az osszes paros elemet adja vissza
    for elem in lista:
        if elem % 2 == 0:
            yield elem

for elem in paros(szamok):
    print(elem, end=" ")
print()

a_pont = 0
b_pont = 0
for i in range(10):
    #a és b dob kockával, aki nagyobbat dob az kap pontot, ha egyenlő akkor mindketten
    a_kocka = random.randint(1, 6)
    b_kocka = random.randint(1, 6)
    if a_kocka > b_kocka:
        a_pont += 1
    elif a_kocka < b_kocka:
        b_pont += 1
    else:
        a_pont += 1
        b_pont += 1

print(f"a pontjai: {a_pont}")
print(f"b pontjai: {b_pont}")

plt.pie([a_pont, b_pont], labels=["A játékos", "B játékos"], autopct="%.2f%%")
plt.show()