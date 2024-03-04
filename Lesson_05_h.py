def matrix_keszit():
    matrix = [
        [1, 2, 3, 4], 
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(len(matrix)) #3
    print(len(matrix[0])) #4

#matrix_keszit()
    
def ures_matrix(sor, oszlop):
    matrix = []
    for i in range(sor):
        seged_sor = []
        for j in range(oszlop):
            seged_sor.append(0)
        matrix.append(seged_sor)
    return matrix

matrix1 = ures_matrix(3, 4)

def kiir(matrix):
    for sor in matrix:
        for elem in sor:
            print(elem, end=" ")
        print()

kiir(matrix1)
print()

matrix1[1][2] = 1

kiir(matrix1)

# 0,0 0,1 0,2 0,3
# 1,0 1,1 1,2 1,3
# 2,0 2,1 2,2 2,3

#Lépések
#1. kell egy 3soros, 4 oszlopos üres mátrix
#2. végig kell menni a teljes mátixon
    # minden egyes elemet felül kell írni a mefelelő számpárral
    # matrix[1][2] = f"{egyes valtozo},{kettes valtzo}"
#3. ki kell iratni a mátrixot

matrix2 = ures_matrix(3, 4)

def szamoz(matrix):
    for i in range(len(matrix)): #sorok szama
        for j in range(len(matrix[i])): #oszlopok szama
            matrix[i][j] = f"{i},{j}"
    return matrix

matrix2 = szamoz(matrix2)

print()
kiir(matrix2)

def magikus_kocka(n):
    matrix = ures_matrix(n, n)
    i = 0
    j = int(n / 2)
    for szam in range(1, 10):
        matrix[i][j] = szam
        uj_i = i - 1
        uj_j = j + 1
        if i == 0:
            uj_i = n - 1
        if j == n - 1:
            uj_j = 0
        if matrix[uj_i][uj_j] != 0:
            i += 1
            #j = j
        else:
            i = uj_i
            j = uj_j
    kiir(matrix)

print()
magikus_kocka(3)
        