from Domain.Obiect import getLocatie, getPret


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