from Test.testCRUD import testAdaugaObiect, testStergeObiect, testModificaObiect
from Test.testDomain import testObiect
from Test.testFunctionalitati import testChangeLocation, testPretMax, testsumaPreturilor, testOrdonareDupaPret, \
    testSchimbaDescrierea
from Test.testUndoRedo import testundoredo


def runAllTests():
    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testModificaObiect()
    testChangeLocation()
    testPretMax()
    testsumaPreturilor()
    testOrdonareDupaPret()
    testSchimbaDescrierea()
    testundoredo()