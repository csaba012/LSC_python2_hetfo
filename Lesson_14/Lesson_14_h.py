import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

def beolvasKiirat():
    csv = pd.read_csv("Lesson_14/library.csv")
    print(csv.head(5))
    print("----------------------------------")
    csv = csv.drop(["Edition Statement", "Contributors", 
                    "Corporate Author", "Corporate Contributors", 
                    "Former owner", "Engraver"], axis=1)
    print(csv.head(5))
    print("----------------------------------")
    csv = csv.drop(columns=["Shelfmarks"])
    print(csv.head(5))

# beolvasKiirat()

def azonosito():
    csv = pd.read_csv("Lesson_14/library.csv")
    print(csv["Identifier"].is_unique)
    csv = csv.set_index("Identifier")
    print(csv.head(5))

# azonosito()

def sor(index): 
    csv = pd.read_csv("Lesson_14/library.csv")
    csv = csv.set_index("Identifier")
    print(csv.loc[index])

# sor(206)

def sor2(sor):
    csv = pd.read_csv("Lesson_14/library.csv")
    csv = csv.set_index("Identifier")
    print(csv.iloc[sor])

# sor2(206)

def takaritas():
    csv = pd.read_csv("Lesson_14/library.csv")
    csv = csv.set_index("Identifier")
    print(csv.loc[1982:, "Date of Publication"].head(20))
    jo_sorok = csv["Date of Publication"].str.extract(r'^(\d{4})', expand=False)
    csv["Date of Publication"] = pd.to_numeric(jo_sorok)
    print(csv.loc[1982:, "Date of Publication"].head(20))
    print(csv["Date of Publication"].isnull().sum() / len(csv))
    atlag = round(csv["Date of Publication"].mean())
    print(atlag)
    csv["Date of Publication"] = csv["Date of Publication"].fillna(atlag)
    print(csv.loc[1982:, "Date of Publication"].head(20))

# takaritas()

def olimpia():
    csv = pd.read_csv("Lesson_14/olympics.csv", header=1)
    print(csv.head(10))
    csv.rename(columns={
        'Unnamed: 0': 'Országok',
        '? Summer': 'Nyári olimpia',
        '? Winter': 'Téli olimpia',
        '? Games': 'Sportágak száma', 
        '01 !': 'Ny_arany', 
        '01 !.1': 'T_arany',
        '01 !.2': 'S_arany'
    }, inplace=True)
    print(csv.head(10))


olimpia()