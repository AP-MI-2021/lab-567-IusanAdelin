from Domain.Obiect import getLocatie, getDescriere, getId
from Logic.CRUD import adaugaObiect, getById
from Logic.Functionalitati import changeLocation, PretMax, Concatenare, sumaPreturilor, OrdonareDupaPret


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

def testSchimbaDescrierea():
    lista = []
    lista = adaugaObiect("1","Telefon", "Vorbesti cu alti oameni", 3000, "CCCC",lista)
    lista = adaugaObiect("2","Masina", "Asigura deplasarea oamenilor pe strada", 30000, "CCCC",lista)
    lista = adaugaObiect("3", "Harta", "Te ajuta sa te ghidezi", 200, "EEEE",lista)
    lista = Concatenare(" asa", lista, 2000)
    assert getDescriere(getById("1", lista)) == "Vorbesti cu alti oameni asa"
    assert getDescriere(getById("2", lista)) == "Asigura deplasarea oamenilor pe strada asa"
    assert getDescriere(getById("3", lista)) == "Te ajuta sa te ghidezi"

def testOrdonareDupaPret():
    lista=[]
    lista = adaugaObiect("1", "Telefon", "Vorbesti cu alti oameni", 3000, "CCCC", lista)
    lista = adaugaObiect("2", "Masina", "Asigura desfasurarea oamenilor pe strada", 30000, "DDDD", lista)
    lista = adaugaObiect("3", "Harta", "Te ajuta sa te ghidezi", 200, "EEEE", lista)
    lista = adaugaObiect("4", "Pix", "obiect de scris", 10, "CCCC", lista)
    lista = adaugaObiect("5", "Lanterna ", "Obiect de iluminat ", 300, "EEEE", lista)
    lista = adaugaObiect("6", "Bicicleta", "Deplasarea", 5000, "DDDD", lista)
    rezultat = OrdonareDupaPret(lista)
    assert getId(rezultat[0]) == "4"
    assert getId(rezultat[1]) == "3"
    assert getId(rezultat[2]) == "5"
    assert getId(rezultat[3]) == "1"
    assert getId(rezultat[4]) == "6"
    assert getId(rezultat[5]) == "2"

def testsumaPreturilor():
    lista=[]
    lista = adaugaObiect("1", "Telefon", "Vorbesti cu alti oameni", 3000, "CCCC", lista)
    lista = adaugaObiect("2", "Masina", "Asigura desfasurarea oamenilor pe strada", 30000, "DDDD", lista)
    lista = adaugaObiect("3", "Harta", "Te ajuta sa te ghidezi", 200, "CCCC", lista)
    rezultat = sumaPreturilor(lista)
    assert len(rezultat) == 2
    assert rezultat["CCCC"] == 3200
    assert rezultat["DDDD"] == 30000