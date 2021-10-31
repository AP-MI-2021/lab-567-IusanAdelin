from Test.testCRUD import testAdaugaObiect, testStergeObiect
from Test.testDomain import testObiect
from Test.testFunctionalitati import testChangeLocation, testPretMax


def runAllTests():
    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testChangeLocation()
    testPretMax()