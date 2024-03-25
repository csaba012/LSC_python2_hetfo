tabla = [
    [0, 7, 0, 0, 9, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 7, 4, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 4, 0],
    [0, 0, 8, 0, 0, 0, 3, 5, 2],
    [0, 0, 0, 0, 4, 2, 0, 9, 1],
    [3, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 2, 0, 4],
    [1, 0, 4, 0, 2, 0, 0, 8, 7]
]

def kiir(tabla):
    for i in range(len(tabla)):
        if i % 3 == 0 and i != 0:
            print("- " * 11)
        for j in range(len(tabla[i])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(tabla[i][j], end=" ")
        print()

def ures_keres(tabla):
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            if tabla[i][j] == 0:
                return (i, j)
    return None

def ellenoriz(tabla, szam, poz):
    for i in range(len(tabla[0])):
        if tabla[poz[0]][i] == szam and poz[1] != i:
            return False
    for i in range(len(tabla)):
        if tabla[i][poz[1]] == szam and poz[0] != i:
            return False
    negyzet_i = poz[0] // 3
    negyzet_j = poz[1] // 3
    for i in range(negyzet_i * 3, negyzet_i * 3 + 3):
        for j in range(negyzet_j * 3, negyzet_j * 3 + 3):
            if tabla[i][j] == szam and (i, j) != poz:
                return False
    return True

def megold(tabla):
    ures_mezo = ures_keres(tabla)
    if not ures_mezo:
        return True
    else:
        i, j = ures_mezo
    
    for szam in range(1, 10):
        if ellenoriz(tabla, szam, (i, j)):
            tabla[i][j] = szam
            if megold(tabla):
                return True
            tabla[i][j] = 0
    return False

kiir(tabla)
megold(tabla)
print()
kiir(tabla)