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