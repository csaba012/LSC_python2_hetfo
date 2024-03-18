import Lesson_07.Alap as sajat
# from Lesson_07 import Alap, Halado
import datetime

#print(sajat.prim_e(5))

# 0 0 0 0
# 0 0 0 0
# 0 0 0 0

# 0,0 0,1 0,2 0,3
# 1,0 1,1 1,2 1,3
# 2,0 2,1 2,2 2,3

# 0 1 2 3
# 1 2 3 4
# 2 3 4 5

# True True True True
# True True True False
# True True False True

def feladat1():
    matrix = sajat.matrix_keszit(3, 4)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = sajat.prim_e(i + j)
    sajat.kiir(matrix)

#feladat1()

print(datetime.date.today())
print(datetime.date.today().strftime("%w"))
print(datetime.date.today().strftime("%Y. %B %d."))