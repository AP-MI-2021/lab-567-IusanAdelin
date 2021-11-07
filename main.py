from Domain.Obiect import creeazaObiect
from Logic.CRUD import adaugaObiect
from Test.TestAll import runAllTests
from UI.console import runMenu
from UI.console2 import runNewMenu, MenuHelp


def meniuri():
    print(" For help type Help")
    print("1. Meniul vechi")
    print("2. Meniul nou")
    print("x. Iesire")

def main():
    runAllTests()

    lista = []
    lista = adaugaObiect(1, "pc", "descriere 1", 4000, "loc1", lista)
    lista = adaugaObiect(2, "laptop", "descriere 2", 1000, "loc1", lista)
    lista = adaugaObiect(3, "birou", "descriere 3", 3000, "loc2", lista)
    lista = adaugaObiect(4, "masa", "descriere 4", 2000, "loc2", lista)

    while True:
        meniuri()
        optiune = input("Dati optiunea: ")
        if optiune == "Help":
            MenuHelp()
        if optiune == "1":
            runMenu(lista)
        elif optiune == "2":
            runNewMenu(lista)

main()