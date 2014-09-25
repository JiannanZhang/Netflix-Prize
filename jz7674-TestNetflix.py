import json
from io import StringIO
from unittest import main,TestCase
from Netflix import getAveAllUsers, getPredictRating, netflixEval

class TestNetflix(TestCase):

    def testAveAllUsers1(self):
        dicFile = {1:2,2:2}
        realPrat = 2
        prat = getAveAllUsers(dicFile)
        self.assertEqual(realPrat, prat)


    def testAveAllUsers2(self):
        dicFile = {1:1,2:5}
        realPrat = 3
        prat = getAveAllUsers(dicFile)
        self.assertEqual(realPrat, prat)


    def testAveAllUsers3(self):
        dicFile = {1:2,2:4}
        realPrat = 3
        prat = getAveAllUsers(dicFile)
        self.assertEqual(realPrat, prat)

    def testAveAllUsers4(self):
        dicFile = {1:2,2:1}
        realPrat = 1.5
        prat = getAveAllUsers(dicFile)
        self.assertEqual(realPrat, prat)


    def testAveAllUsers5(self):
        dicFile = {1:5,2:5}
        realPrat = 5
        prat = getAveAllUsers(dicFile)
        self.assertEqual(realPrat, prat)


    def testAveAllUsers6(self):
        dicFile = {1:10,2:10}
        realPrat = 10
        prat = getAveAllUsers(dicFile)
        self.assertEqual(realPrat, prat)

    def testAveAllUsers7(self):
        dicFile = {1:8,2:2}
        realPrat = 5
        prat = getAveAllUsers(dicFile)
        self.assertEqual(realPrat, prat)
   
    def testAveAllUsers8(self):
        dicFile = {1:10,2:5}
        realPrat = 7.5
        prat = getAveAllUsers(dicFile)
        self.assertEqual(realPrat, prat)


    def testAveAllUsers9(self):
        dicFile = {1:3,2:3}
        realPrat = 3
        prat = getAveAllUsers(dicFile)
        self.assertEqual(realPrat, prat)


    def testPredictRating1(self):
        testPredict = float('%.1f'% getPredictRating('1','6'))
        assert type(testPredict) == float
        realPredict = 3.5
        self.assertEqual(testPredict, realPredict)

    def testPredictRating2(self):
        testPredict = float('%.1f'% getPredictRating('1','8'))
        assert type(testPredict) == float
        realPredict = 4.3
        self.assertEqual(testPredict, realPredict)

    def testPredictRating3(self):
        testPredict = float('%.1f'% getPredictRating('1','7'))
        assert type(testPredict) == float
        realPredict = 4.1
        self.assertEqual(testPredict, realPredict)

    def testNetflixEval(self):
        r = StringIO("1:\n30878\n14756")
        w = StringIO()
        rmse = float('%.2f' %netflixEval(r,w))
        self.assertEqual(rmse, 0.97)


main()
















