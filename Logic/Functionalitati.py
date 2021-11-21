from Domain.Obiect import getLocatie, getPret, getId, getNume, getDescriere, creeazaObiect


def changeLocation(locatieVeche, locatieNoua, lista):
    '''
    Mutarea tuturor obiectelor intr-o anumita locatie.
    :param locatie:
    :param lista:
    :return:
    '''


    for obiect in lista:
        if getLocatie(obiect) == locatieVeche:
            obiect["locatie"] = locatieNoua

    return lista

def OrdonareDupaPret(lista):
    '''
    Ordonarea obiectelor crescător după prețul de achiziție.
    :param lista: lista de obiecte
    :return: Obiectele ordonate crescator dupa pretul de achizitie
    '''
    return sorted(lista, key=lambda obiect: getPret(obiect))

def sumaPreturilor(lista):
    '''
    Afișarea sumelor prețurilor pentru fiecare locație.
    :param lista: lista de obiecte
    :return: suma preturilor pentru fiecare locatie
    '''
    rezultat = {}
    for obiect in lista:
            locatie = getLocatie(obiect)
            if locatie in rezultat:
                rezultat[locatie] = rezultat[locatie] + getPret(obiect)
            else:
                rezultat[locatie] = getPret(obiect)
    return rezultat

def PretMax(lista):
    '''
    Determinarea celui mai mare preț pentru fiecare locație
    :param lista: lista de obiecte
    :return: Cel mai mare preț pentru fiecare locație
    '''
    rezultat = {}
    for obiect in lista:
        locatie = getLocatie(obiect)
        if locatie in rezultat:
             if getPret(obiect) > rezultat[locatie]:
                rezultat[locatie] = getPret(obiect)
        else:
            rezultat[locatie] = getPret(obiect)
    return rezultat

def Concatenare(text, lista, pret):
    '''
    Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită
    :param text: stringul care trebuie adaugat la descrierile obiectelor cu pretul mai mare decat o valoare citita
    :param lista: lista de obiecte
    :param pret: valoarea dupa care comparam pretul fiecarui obiect pt a verifica daca ii modificam descrierea
    :return: o lista noua in care toate descrierile obiectelor cu pretul mai mare decat valoarea data au fost modificate, concatenandu-se un string
    '''
    listaNoua = []
    for obiect in lista:
        if getPret(obiect) > pret:
            obiectNou = creeazaObiect(
                getId(obiect),
                getNume(obiect),
                getDescriere(obiect) + str(text),
                getPret(obiect),
                getLocatie(obiect)
             )
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua
