def matrix_keszit(sor, oszlop):
    return [[0 for i in range(oszlop)] for j in range(sor)]

def kiir(matrix):
    for sor in matrix:
        for elem in sor:
            print(elem, end=" ")
        print()
    print()

def prim_e(szam):
    #adjon vissza igazat, ha prim a szam (csak 1-gyel és önmagával osztható)
    #adjon vissza hamisat, ha nem prím a szam (van más osztója is)
    
    # 1 2 3 4 5 - prim
    # + - - - +

    # 1 2 3 4 5 6 - nem prim
    # + + 

    for oszto in range(2, szam):
        if szam % oszto == 0:
            return False
    return True 