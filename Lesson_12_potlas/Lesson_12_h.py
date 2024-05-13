def beolvasTeljes():
    f = open("Lesson_12_potlas/szoveg.txt", "r", encoding="utf-8")
    print(f.read())
    f.close()

# beolvasTeljes()

def fajlbaIr(nev, szoveg):
    with open(f"Lesson_12_potlas/{nev}.txt", "w", encoding="utf-8") as f:
        f.write(szoveg)

# fajlbaIr("teszt", "alma, körte, szilva")

def fajlbaKiegeszit():
    with open("Lesson_12_potlas/teszt.txt", "a", encoding="utf-8") as f:
        for i in range(10):
            f.write(str(i) + "\n")

# fajlbaKiegeszit()

def beolvasSort():
    with open("Lesson_12_potlas/szoveg.txt", "r", encoding="utf-8") as f:
        #print(f.readlines())
        print(f.readline())
        f.seek(0)
        print(f.readline())

beolvasSort()