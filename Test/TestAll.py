from Test.testCRUD import testAdaugaObiect, testStergeObiect, testModificaObiect
from Test.testDomain import testObiect
from Test.testFunctionalitati import testChangeLocation, testPretMax


def runAllTests():
    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testModificaObiect()
    testChangeLocation()
    testPretMax()