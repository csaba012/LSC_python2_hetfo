def fugg(param1):
    if type(param1) == int:
        return param1 * 2 
    
    return param1

def szorzo(szam):
    if szam <= 0:
        return 
    print(szam * 3)
    print(szam + 5)


def szorzo2(szam):
    if szam > 0:
        print(szam * 3)
        print(szam + 5)

#szoveg = fugg()
#print(szoveg)
#print(fugg(1+2))
#print(fugg("szia"))
#print(szorzo(2))
#print(szorzo(-1))

def fugg2(p1, p2, p3):
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"p3: {p3}")
fugg2(p2= 2, p3= 3, p1= 1)

def paros(szam):
    if type(szam) != int:
        return "nem szám"
    if szam % 2 == 0:
        return "páros"
    else:
        return "páratlan"

print(paros(1)) #páratlan
print(paros(2)) #páros
print(paros("alma")) #nem szám
print(paros(False)) #nem szám

def prim(szam):
    for i in range(2, szam):
        if szam % i == 0:
           return False
    return True

if(prim(2)):
    print("prím")
else:
    print("nem prím")

def penz(ertek, arfolyam = 380, penznem = "Ft"):
    if penznem == "Ft":
        print(f"{ertek} {penznem}")
    elif penznem == "Euro":
        print(f"{ertek * arfolyam} {penznem}")

penz(1500, "Ft")
penz(1500)
penz(1500, 380, "Euro")