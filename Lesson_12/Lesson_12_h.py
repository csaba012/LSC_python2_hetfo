import os

def beolvas():
    f = open("Lesson_12/szoveg.txt", "r", encoding="utf-8")
    tartalom = f.read()
    print(tartalom)
    f.close()

#beolvas()

def beolvasKarakterek(db):
    f = open("Lesson_12/szoveg.txt", "r", encoding="utf-8")
    print(f.read(db))
    f.seek(0)
    print(f.read(db))
    f.close()

#beolvasKarakterek(6)

def beolvasSoronkent():
    f = open("Lesson_12/szoveg.txt", "r")
    sorok = f.readlines()
    print(sorok[3])
    f.close()

#beolvasSoronkent()

def keres(szo):
    with open("Lesson_12/szoveg.txt", "r") as f:
        if szo in f.read():
            print("benne van")
        else:
            print("nincs benne")

#keres("and")

def fajlLetrehoz(nev):
    f = open(f"Lesson_12/{nev}.txt", "w")
    f.close()

#fajlLetrehoz("teszt")

def fajlIras(nev, szoveg):
    with open(f"Lesson_12/{nev}.txt", "w+") as f:
        f.write(szoveg)
        f.seek(0)
        print(f.read())

#fajlIras("teszt", "Logiscool alma körte\nszilva cica")

def egyTiz(nev):
    #ird ki a nev nevezetű fájlba 1-től 10-ig a számokat, minden szám új sorba
    with open(f"Lesson_12/{nev}.txt", "w") as f:
        for szam in range(1, 11):
            f.write(str(szam) + "\n")

#egyTiz("teszt")

def vegerolOlvas(db):
    with open("Lesson_12/szoveg.txt", "r") as f:
        sorok = f.readlines()
        while db > 0:
            print(sorok[-db])
            db -= 1

#vegerolOlvas(4)

def hozzafuz(nev, szoveg):
    with open(f"Lesson_12/{nev}.txt", "a+") as f:
        f.write(szoveg + "\n")
        f.seek(0)
        print(f.read())
    
#hozzafuz("teszt", "alma")

def tempFajl():
    with open("Lesson_12/szoveg.txt", "r+") as f:
        sor = f.readline()
        sor = sor.replace(" ", "_")
        sor = sor.lower()
        with open("Lesson_12/temp.txt", "w") as temp_f:
            temp_f.write(sor)
        #valahol mashol egy masik fuggvenyben 
        with open("Lesson_12/temp.txt", "r") as temp_f:
            print(temp_f.read())
        os.remove("Lesson_12/temp.txt")

tempFajl()