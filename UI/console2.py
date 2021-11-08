from Domain.Obiect import creeazaObiect, toString
from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect
from Logic.Functionalitati import changeLocation
from UI.console import uiAdaugaObiect


def MenuHelp():
    print("Spre exemplu pentru comenzi din"
          "CRUD:add,id, nume, descriere, pret, locatie")
    print("Pentru afisarea tuturor obiectelor :showall")
    print("Pentru mutarea dintr-o locatie in alta a obiectelor:mutare,locatie_initiala,locatie_noua")
    print("Iar pentru folosirea mai multor actiuni la o singura citire vom proceda astfel:add,id, nume, "
          "descriere, pret, locatie;show_all;mutare,locatieInitiala,locatieNoua")

def add(id, nume, descriere, pret, locatie, lista):

    try:
        lista = adaugaObiect(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
    print("Obiectul a fost adaugata")
    return lista

def delete(id, lista):
    try:
        lista = stergeObiect(id, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
    print("Stergerea a fost facuta")
    return lista

def showall(lista):
    for obiect in lista:
        print(toString(obiect))

def modify(id, nume, descriere, pret, locatie, lista):
    try:
        lista = modificaObiect(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
    print("Modificarea a fost facuta")
    return lista



def runNewMenu(lista):
    while True:
        optiune = input("Dati comenzile: ")
        optiuni = optiune.split(';')
        for comenzi in optiuni:
            sir = comenzi.split(',')
            if sir[0] == "add":
                id = sir[1]
                nume = sir[2]
                descriere = sir[3]
                pret = sir[4]
                locatie = sir[5]
                lista = add(id, nume, descriere, pret, locatie, lista)
            if sir[0] == "delete":
                id = int(sir[1])
                lista = delete(id, lista)
            if sir[0] == "showall":
                showall(lista)
            if sir[0] == "modify":
                id = sir[1]
                nume = sir[2]
                descriere = sir[3]
                pret = sir[4]
                locatie = sir[5]
                lista = modify(id, nume, descriere, pret, locatie, lista)