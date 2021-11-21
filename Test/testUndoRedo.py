from Domain.Obiect import getId
from Logic.CRUD import adaugaObiect, getById
from Logic.Functionalitati import changeLocation, Concatenare


def testundoredo():
    redoList = []
    lista = []
    undoList = []

   #creez o lista noua pentru a memora pasul anterior
    rezultat = adaugaObiect("1", "masa", "se poate manca pe ea", 250, "aici", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat  # retin obiectul adaugat in lista
    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"

    rezultat = adaugaObiect("2","scaun","poti sta pe el",100, "asma",lista )
    undoList.append(lista) #daca vreau sa fac undo retin [[],[1]]
    redoList.clear()
    lista = rezultat #retin obiectul adaugat in lista
    assert len(lista) == 2

    rezultat = adaugaObiect("3", "pix", "poti scrie cu el", 40, "acsc", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    assert len(lista) == 3

    redoList.clear()
    #functia pop scoate ultimul element din lista de liste
    lista = undoList.pop()

    #daca mai facem un undo, atunci o sa dispara si ultima lista [[1]]
    redoList.append(lista)
    lista = undoList.pop()
    assert undoList == [[]]

    #daca se mai face un undo, dispare si lista vida
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == []

    #inca un undo, nu modifica nimic. am pus conditia de if, pt ca lungimea listei este 0, altfel avem eroare
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == []

    #acum lista initiala este vida, caci am anulat operatiile de adaugare
    assert lista == []
    rezultat = adaugaObiect("4","fotoliu","poti sta pe el", 700, "ascd", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()
    assert redoList == []

    rezultat = adaugaObiect("5", "creion", "poti scrie cu el", 20, "ssaa", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    rezultat = adaugaObiect("6", "veioza", "iti face lumina", 100, "asas", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    assert len(lista) == 3

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert redoList == []
    assert len(redoList) == 0


    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[]]


    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 1

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 0
    if len(undoList) > 0:
        redoList.append(lista)
    lista = undoList.pop()

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[]]

    rezultat = adaugaObiect("7", "sticla", "poti depozita apa in ea", 25, "asss", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()
    assert len(lista) == 2
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()


    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[]]


    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == []


    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 1
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2


    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 0

#teste pentru functionalitati
 #1.test pt concatenarea unui string citit la toate descrierile cu pret mai mare
    rezultat = Concatenare("sa concatenam textul", lista, 10)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    rezultat = Concatenare("alt text",lista, 7)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    rezultat = Concatenare("asd", lista, 7)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat
    #se face un undo
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    # se face un undo
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    #se face un redo

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[]]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == []

#2. test pentru Mutati obiectele dintr-o locatie in alta
    rezultat = adaugaObiect("1", "masa", "se poate manca pe ea", 250, "aici", lista)
    undoList.append(lista)
    redoList.append(lista)
    lista = rezultat

    rezultat = adaugaObiect("2", "scaun", "poti sta pe el", 100, "asma", lista)
    undoList.append(lista)
    redoList.append(lista)
    lista = rezultat

    rezultat = changeLocation("aici", "aaaa", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    rezultat = changeLocation("aaaa", "bbbb", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    rezultat = changeLocation("bbbb", "cccc", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    #se face un undo
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    #se face inca un undo
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    #se face un redo

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
