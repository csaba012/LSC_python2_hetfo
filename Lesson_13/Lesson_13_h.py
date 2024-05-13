import pandas as pd

def megnyitas():
    csv_fajl = pd.read_csv("Lesson_13/oscar_age_female.csv")
    print(csv_fajl.head(20))

#megnyitas()

def eletkorNev():
    csv = pd.read_csv("Lesson_13/oscar_age_female.csv", usecols=["Age", "Name"])
    print(csv.head(10))
    osszeg = csv["Age"].sum()
    db = len(csv["Age"])
    atlag = osszeg / db
    print(f"Átlagosan {round(atlag, 2)} évesen kapnak oscar díjat a színésznők.")

#eletkorNev()

def legidosebb():
    csv = pd.read_csv("Lesson_13/oscar_age_female.csv", usecols=["Age", "Name"])
    max_eletkor = max(csv["Age"])
    sor = csv[csv["Age"] == max_eletkor]
    print(f"{sor.iloc[0, 1]} volt a legidősebb szinésznő, {sor.iloc[0, 0]} éves")

# legidosebb()

def fargoNyertes():
    # melyik éveben nyert oscar dijat a "Fargo" című film
    # 1997
    csv = pd.read_csv("Lesson_13/oscar_age_female.csv", usecols=["Year", "Movie"], skipinitialspace=True)
    sor = csv[csv["Movie"] == "Fargo"]
    print(f"A Fargo című film {sor.iloc[0, 0]}-ben kapott oscar díjat")

# fargoNyertes()

def gyakoribb(szazalek):
    csv = pd.read_csv("Lesson_13/letter_frequency.csv", skipinitialspace=True)
    db = 0
    for index, sor in csv.iterrows():
        if sor["Percentage"] >= szazalek:
            db += 1
            print(f"{ sor['Letter'] } - {sor['Percentage']}%")
    print(f"{db} db ilyen betűt találtunk")

# gyakoribb(4)

def maganhangzok():
    #a maganhangzok osszesített előfordulását akarom tudni százalékban
    maganhangzok_lista = ["A", "E", "I", "O", "U"]
    csv = pd.read_csv("Lesson_13/letter_frequency.csv", skipinitialspace=True)
    ossz = 0
    for index, sor in csv.iterrows():
        if sor["Letter"] in maganhangzok_lista:
            ossz += sor["Percentage"]
    print(round(ossz, 1))

# maganhangzok()

def huzas():
    csv = pd.read_csv("Lesson_13/secret_santa.csv", skipinitialspace=True)
    kevert = csv.sample(frac=1)
    kevert.to_csv("Lesson_13/kevert.csv")
    uj_csv = pd.read_csv("Lesson_13/kevert.csv", skipinitialspace=True)
    for index, sor in csv.iterrows():
        ki = sor["Name"]
        kinek = uj_csv["Name"][index]
        print(f"{ki} ajándékot vesz {kinek}-nek")

huzas()