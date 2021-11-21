from Domain.Obiect import toString
from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect
from Logic.Functionalitati import changeLocation, PretMax, Concatenare, OrdonareDupaPret, sumaPreturilor


def printMenu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiecte")
    print("4. Mutarea tuturor obiectelor intr-o locatie")
    print("5. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.")
    print("6. Determinarea celui mai mare preț pentru fiecare locație")
    print("7. Ordonarea obiectelor crescator dupa pretul de achizitie ")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare obiecte")
    print("x. Iesire")


def uiAdaugaObiect(lista,undoList,redoList):
    try:
        id=input("Dati id-ul ")
        nume=input("Dati numele ")
        descriere=input("Dati descrierea ")
        pret=float(input("Dati pretul "))
        locatie=input("Dati locatia ")

        rezultat=adaugaObiect(id, nume, descriere, pret, locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeObiect(lista, undoList, redoList):
    try:
        id = input("Dati id-ul obiectului pe care vreti sa il stergeti ")
        rezultat=stergeObiect(id,lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaObiect(lista,undoList, redoList):
    try:
        id = input("Dati id-ul obiectului de modificat ")
        nume = input("Dati noul nume ")
        descriere = input("Dati noua descriere ")
        pret = float(input("Dati noul pret "))
        locatie = input("Dati noua locatie ")
        rezultat=modificaObiect(id, nume, descriere, pret, locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiChangeLocation(lista):
    locatieNoua = input("Dati locatia noua: ")
    locatieVeche = input("Alegeti locatia obiectelor pe care vreti sa le mutati: ")
    return changeLocation(locatieVeche, locatieNoua, lista)

def uiPretMax(lista):
    rezultat = PretMax(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie, rezultat[locatie]))

def uiConcatenare(lista,undoList,redoList):
    try:
        substring = input("Dati stringul de la tastatura: ")
        pret = float(input("Dati pretul: "))
        rezultat = Concatenare(substring,lista,pret)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiOrdoneaza(lista):
    showAll(OrdonareDupaPret(lista))

def uiSumaPreturilor(lista):
    rezultat = sumaPreturilor(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))


def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune=input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaObiect(lista,undoList,redoList)
        elif optiune =="2":
            lista= uiStergeObiect(lista,undoList,redoList)
        elif optiune == "3":
            lista = uiModificaObiect(lista,undoList,redoList)
        elif optiune =="4":
            lista = uiChangeLocation(lista)
        elif optiune == "5":
            lista = uiConcatenare(lista, undoList, redoList)
        elif optiune == "6":
            uiPretMax(lista)
        elif optiune == "7":
            uiOrdoneaza(lista)
        elif optiune == "8":
            uiSumaPreturilor(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresit! Reincercati: ")