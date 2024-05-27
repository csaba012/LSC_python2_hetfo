import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

def beolvas():
    csv = pd.read_csv("Lesson_14_potlas/library.csv")
    print(csv.head(5))
    print("-----------------------")
    csv = csv.drop(["Corporate Contributors", "Former owner", "Engraver"], axis=1)
    print(csv.head(5))
    print("-----------------------")
    csv = csv.drop(columns=["Corporate Author"])
    print(csv.head(5))

# beolvas()

def index():
    csv = pd.read_csv("Lesson_14_potlas/library.csv")
    print(csv["Identifier"].is_unique)
    csv = csv.set_index("Identifier")
    print(csv.head(5))

# index()

def keres(index):
    csv = pd.read_csv("Lesson_14_potlas/library.csv")
    csv = csv.set_index("Identifier")
    print(csv.loc[index])

keres(206)