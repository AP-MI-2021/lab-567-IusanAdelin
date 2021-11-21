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
    lista = rezultat #retin obiectul adaugat in lista
    assert len(lista) == 1
    assert lista == [["1", "masa", "se poate manca pe ea", 250, "aici"]]
    assert getId(getById("1", lista)) == "1"

    rezultat = adaugaObiect("2","scaun","poti sta pe el",100, "asma",lista )
    undoList.append(lista) #daca vreau sa fac undo retin [[],[1]]
    redoList.clear()
    lista = rezultat #retin obiectul adaugat in lista
    assert len(lista) == 2
    assert lista == [["1", "masa", "se poate manca pe ea", 250, "aici"],["2","scaun","poti sta pe el",100, "asma"]]

    rezultat = adaugaObiect("3", "pix", "poti scrie cu el", 40, "acsc", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    assert len(lista) == 3
    assert lista == [["1", "masa", "se poate manca pe ea", 250, "aici"],
                     ["2", "scaun", "poti sta pe el", 100, "asma"],
                     ["3", "pix", "poti scrie cu el", 40, "acsc"]]

    redoList.clear()
    #functia pop scoate ultimul element din lista de liste
    lista = undoList.pop()
    #la inceput, inainte de undo, mai aveam si lista [[1],[2]], dar dupa undo, vom avea [[],[1]]
    assert undoList == [[],[["1", "masa", "se poate manca pe ea", 250, "aici"]]]

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
    assert lista == [["4","fotoliu","poti sta pe el", 700, "ascd"]]

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
    assert undoList == [[],[["4","fotoliu","poti sta pe el", 700, "ascd"]]]


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
    assert undoList == [[], [["4", "fotoliu", "poti sta pe el", 700, "ascd"]]]

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
    assert undoList == [[],[["4", "fotoliu", "poti sta pe el", 700, "ascd"]]]


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
    assert lista == [['4', 'fotoliu', 'poti sta pe elsa concatenam textul', 700, 'ascd'], ['7', 'sticla', 'poti depozita apa in easa concatenam textul', 25, 'asss']]

    rezultat = Concatenare("alt text",lista, 7)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat
    assert lista == [['4', 'fotoliu', 'poti sta pe elsa concatenam textulalt text', 700, 'ascd'], ['7', 'sticla', 'poti depozita apa in easa concatenam textulalt text', 25, 'asss']]

    rezultat = Concatenare("asd", lista, 7)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat
    #se face un undo
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[], [['4', 'fotoliu', 'poti sta pe el', 700, 'ascd']], [['4', 'fotoliu', 'poti sta pe el', 700, 'ascd'], ['7', 'sticla', 'poti depozita apa in ea', 25, 'asss']], [['4', 'fotoliu', 'poti sta pe elsa concatenam textul', 700, 'ascd'], ['7', 'sticla', 'poti depozita apa in easa concatenam textul', 25, 'asss']]]

    # se face un undo
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[], [['4', 'fotoliu', 'poti sta pe el', 700, 'ascd']], [['4', 'fotoliu', 'poti sta pe el', 700, 'ascd'], ['7', 'sticla', 'poti depozita apa in ea', 25, 'asss']]]

    #se face un redo

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert redoList == [[['4', 'fotoliu', 'poti sta pe elsa concatenam textulalt textasd', 700, 'ascd'], ['7', 'sticla', 'poti depozita apa in easa concatenam textulalt textasd', 25, 'asss']]]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    assert undoList == [[], [['4', 'fotoliu', 'poti sta pe el', 700, 'ascd']], [['4', 'fotoliu', 'poti sta pe el', 700, 'ascd'], ['7', 'sticla', 'poti depozita apa in ea', 25, 'asss']]]
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[], [['4', 'fotoliu', 'poti sta pe el', 700, 'ascd']]]
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
    assert undoList == [[], [['1', 'masa', 'se poate manca pe ea', 250, 'aici']], [['1', 'masa', 'se poate manca pe ea', 250, 'aici'], ['2', 'scaun', 'poti sta pe el',100, 'asma']], [['1', 'masa', 'se poate manca pe ea', 250, 'aaaa'], ['2', 'scaun', 'poti sta pe el', 100, 'asma']]]
    #se face inca un undo
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[], [['1', 'masa', 'se poate manca pe ea', 250, 'aici']], [['1', 'masa', 'se poate manca pe ea', 250, 'aici'], ['2', 'scaun', 'poti sta pe el', 100, 'asma']]]

    #se face un redo

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert redoList == [[['1', 'masa', 'se poate manca pe ea', 250, 'cccc'], ['2', 'scaun', 'poti sta pe el', 100, 'asma']]]