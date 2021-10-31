from Domain.Obiect import getLocatie, getPret, getDescriere, getNume, getId
from Logic.CRUD import adaugaObiect, getById, stergeObiect


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