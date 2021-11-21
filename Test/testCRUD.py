from Domain.Obiect import getLocatie, getPret, getDescriere, getNume, getId
from Logic.CRUD import adaugaObiect, getById, stergeObiect, modificaObiect
from Logic.Functionalitati import sumaPreturilor, OrdonareDupaPret


def testAdaugaObiect():
    lista = []
    lista = adaugaObiect("1", "Creta", "Alba", 10, "Cls1", lista)

    assert len(lista)==1
    assert getId(getById("1",lista)) == "1"
    assert getNume(getById("1",lista)) == "Creta"
    assert getDescriere(getById("1",lista)) == "Alba"
    assert getPret(getById("1",lista)) == 10
    assert getLocatie(getById("1",lista)) == "Cls1"

def testStergeObiect():
    lista = []
    lista = adaugaObiect("1", "Creta", "Alba", 10, "Cls1", lista)
    lista = adaugaObiect("2", "Burete", "De tabla", 5, "Cls2", lista)

    lista = stergeObiect("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

def testModificaObiect():
    lista = []
    lista= adaugaObiect("1", "Creta", "Alba", 10, "Cls1", lista)
    lista= adaugaObiect("2", "Burete", "De tabla", 5, "Cls2", lista)

    lista = modificaObiect("2", "Burete", "Special", 10, "Cls2", lista)

    ObiectNou = getById("2", lista)

    assert getId(ObiectNou) == "2"
    assert getNume(ObiectNou) == "Burete"
    assert getDescriere(ObiectNou) == "Special"
    assert getPret(ObiectNou) == 10
    assert getLocatie(ObiectNou) == "Cls2"

    ObiectVechi = getById("1", lista)

    assert getId(ObiectVechi) == "1"
    assert getNume(ObiectVechi) == "Creta"
    assert getDescriere(ObiectVechi) == "Alba"
    assert getPret(ObiectVechi) == 10
    assert getLocatie(ObiectVechi) == "Cls1"

