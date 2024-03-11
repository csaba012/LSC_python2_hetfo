import matplotlib.pyplot as plt
import numpy as np
import random

def lista_keszit():
    lista = []
    for i in range(6, 14):
        lista.append(i)
    print(lista)

    lista2 = [i for i in range(6, 14)]
    print(lista2)

#lista_keszit()

def paros_lista_keszit():
    lista = [i for i in range(101) if i % 2 == 0]
    print(lista)

#paros_lista_keszit()

def matrix_keszit(sor, oszlop):
    matrix = [[0 for i in range(oszlop)] for j in range(sor)]
    return matrix

def kiir(matrix):
    for sor in matrix:
        for elem in sor:
            print(elem, end=" ")
        print()
    print()

#kiir(matrix_keszit(3, 5))

def matrixok():
    matrix1 = [[i for i in range(10)] for j in range(10)]
    matrix2 = [[j for i in range(10)] for j in range(10)]
    kiir(matrix1)
    kiir(matrix2)

#matrixok()

def idojaras():
    honap = [[random.randint(-5, 22) for i in range(24)] for j in range(31)]
    atlag_homersekletek = [round(np.mean(nap), 2) for nap in honap]
    legmelegebb = np.max(atlag_homersekletek)
    havi_atlag = round(np.mean(atlag_homersekletek), 2)
    print(f"A napi átlag hőmérsékletek: {atlag_homersekletek}")
    print(f"A legmelegebb nap {atlag_homersekletek.index(legmelegebb) + 1}, ekkor {legmelegebb}fok volt")
    print(f"A havi átlag kőmérséklet: {havi_atlag}fok")

idojaras()

def kocka():
    meretek = [5, 5, 5]
    adat = np.ones(meretek)
    szinek = np.empty(meretek + [4])

    szinek[0] = [1, 0, 0, 0.7] #piros
    szinek[1] = [0, 1, 0, 0.7] #zold
    szinek[2] = [0, 0, 1, 0.7] #kek
    szinek[3] = [1, 1, 0, 0.7] #sarga
    szinek[4] = [1, 1, 1, 0.7] #szurke

    fig = plt.figure()
    ertekter = fig.add_subplot(111, projection="3d")
    ertekter.voxels(adat, facecolors=szinek, edgecolors="grey")
    plt.show()

kocka()

