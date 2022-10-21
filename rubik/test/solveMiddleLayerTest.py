'''
Created on Oct 19, 2022

@author: Martin
'''
import unittest
import rubik.solve as solve


class solveMiddleLayerTest(unittest.TestCase):
    

    # def test_solve_040_SolvingTheMiddleLayer_ComplexScramble(self):
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'ybwrbgoyyowgwrybwroowogggwbrggyobygwbbyryrrygbroowbrow' #Scrambled
    #
    #     expectedResult = {}
    #     expectedResult['cube'] = list('gbybbbbbbgryrrrrrrbyyggggggoyrooooooborgyyyyowwwwwwwww')
    #     expectedResult['solution'] = 'ffrFDRRLLblBDLLUUfFFUURRUUBBUULLbuBUUUufUFruRUruRUubuuBUbuBUluLUluLUURurufUFUUURurufUFUUuurURUBubuFufulULuuubUBULulUFufulUL' 
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #

        
    def test_solve_001_FindCorrectMiddleEdge(self):
        inputDict = {}
        inputDict['cube'] = 'rybobbbbbyygrrrrrryboggbgggyybyogooogoroyrygowwwwwwwww'
    
        expectedResult = 8
        actualResult = solve._findMiddleEdge(inputDict['cube'], 22, 31)
        self.assertEqual(actualResult, expectedResult)
    #
    #
    # def test_solve_001_FindCorrectMiddleEdge(self):
    #     inputDict = {}
    #     inputDict['cube'] = 'oyyobrbbbggbbryrrrrbyggbgggryyyogooogoyryrboowwwwwwwww'
    #
    #     expectedResult = 5
    #     actualResult = solve._findMiddleEdge(inputDict['cube'], 4, 13)
    #     self.assertEqual(actualResult, expectedResult)
    #


        
        