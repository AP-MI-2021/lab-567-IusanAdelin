from Domain.Obiect import creeazaObiect, getId


def adaugaObiect(id, nume, descriere, pret, locatie, lista):
    """
    adauga un obiect
    :param id:string
    :param nume:string
    :param descriere:string
    :param pret:float
    :param locatie:string
    :param lista: lista de obiecte
    :return:o lista continand atat obiectele vechi, cat si noul obiect
    """
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja")
    if len(locatie) != 4:
        raise ValueError("Locatia introdusa trebuie sa contina exact 4 caractere")
    if pret < 0:
        raise ValueError("Pretul nu poate fi negativ!")
    obiect = creeazaObiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]

def getById(id, lista):
    """
    da obiectul cu id-ul dat dintr-o lista
    :param id: string
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat din lista sau None daca acesta nu exista
    """
    for obiect in lista:
        if getId(obiect) == id:
            return obiect
    return None

def stergeObiect(id, lista):
    """

    :param id: string
    :param lista:lista de obiecte
    :return: lista fara obiectul cu id-ul dat
    """

    if getById(id, lista) is None:
        raise ValueError("Nu exista obiectul cu Id-ul dat")
    return [obiect for obiect in lista if getId(obiect) != id]

def modificaObiect(id, nume, descriere, pret, locatie, lista):
    """
    modifica un obiect dupa id
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: modifica un obiect dupa id
    """

    if getById(id, lista) is None:
        raise ValueError("Nu exista obiectul cu Id-ul dat")
    listaNoua = []
    for obiect in lista:
        if getId(obiect)== id:
            obiectNou=creeazaObiect(id, nume, descriere, pret, locatie)
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua