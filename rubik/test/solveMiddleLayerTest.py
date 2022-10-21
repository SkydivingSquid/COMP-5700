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

        
    def test_solve_040_FindCorrectMiddleEdge(self):
        inputDict = {}
        cube = 'rybobbbbbyygrrrrrryboggbgggyybyogooogoroyrygowwwwwwwww'
    
        expectedResult = 8
        actualResult = solve._findMiddleEdge(cube, 22, 31)
        self.assertEqual(actualResult, expectedResult)


    def test_solve_041__MoveMiddleEdgeToTopSide(self):
        inputDict = {}
        cube = 'rybobbbbbyygrrrrrryboggbgggyybyogooogoroyrygowwwwwwwww'
        solution = ''
        cubeLocation = 8
        
        expectedResult = {}
        expectedResult['cube'] = list('yybrbbbbbroorrrrrrboyggbggggygyoyoooobygygroywwwwwwwww')
        expectedResult['solution'] = 'uFufulUL'
        expectedResult['cubeLocation'] = 2
        
        actualResult= solve._moveMiddleEdgeToTopSide(cube, solution, cubeLocation)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('cubeLocation'), actualResult.get('cubeLocation'))
        
        
        