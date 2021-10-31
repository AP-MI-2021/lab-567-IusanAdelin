from Domain.Obiect import creeazaObiect, getId, getNume, getDescriere, getPret, getLocatie


def testObiect():
    obiect = creeazaObiect("1", "Creta", "Alba", 10, "Cls1")

    assert getId(obiect) == "1"
    assert getNume(obiect) == "Creta"
    assert getDescriere(obiect) == "Alba"
    assert getPret(obiect) == 10
    assert getLocatie(obiect) == "Cls1"
