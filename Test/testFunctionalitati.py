from Domain.Obiect import getLocatie
from Logic.CRUD import adaugaObiect
from Logic.Functionalitati import changeLocation, PretMax


def testChangeLocation():
    lista = []
    lista = adaugaObiect(1, "pc", "descriere 1", 4000, "loc1", lista)
    lista = adaugaObiect(2, "laptop", "descriere 2", 1000, "loc1", lista)
    lista = adaugaObiect(3, "birou", "descriere 3", 3000, "loc2", lista)
    lista = adaugaObiect(4, "masa", "descriere 4", 2000, "loc2", lista)
    lista = changeLocation("loc1", "loc2", lista)
    assert getLocatie(lista[0]) == "loc2"
    assert getLocatie(lista[1]) == "loc2"

def testPretMax():
    lista = []
    lista = adaugaObiect(1, "tabla", "descriere 1", 3000, "loc1", lista)
    lista = adaugaObiect(2, "laptop", "descriere 2", 2000, "loc1", lista)
    lista = adaugaObiect(3, "scaun", "descriere 3", 200, "loc2", lista)
    rezultat = PretMax(lista)

    assert len(rezultat) == 2
    assert rezultat["loc1"] == 3000
    assert rezultat["loc2"] == 200