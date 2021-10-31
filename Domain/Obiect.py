def creeazaObiect(id, nume, descriere, pret, locatie):
    """
    Creaza un dictionar ce reprezinta obiectele din inventar
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret:  float
    :param locatie: string
    :return: un dictionar ce reprezinta un obiect
    """
    return {
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret,
        "locatie": locatie
    }

def getId(obiect):
    """
    da id-ul unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: id-ul obiectului
    """
    return obiect["id"]

def getNume(obiect):
    return obiect["nume"]

def getDescriere(obiect):
    return obiect["descriere"]

def getPret(obiect):
    return obiect["pret"]

def getLocatie(obiect):
    return obiect["locatie"]

def toString(obiect):
    return "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Locatie: {}".format(
        getId(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPret(obiect),
        getLocatie(obiect)
    )