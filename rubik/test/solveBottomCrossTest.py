'''
Created on Sep 25, 2022

@author: Martin
'''
import unittest
import rubik.solve as solve


class solveBottomCrossTest(unittest.TestCase):
    
    
    #Passing in a solved cube and returning an empty string
    #Passing in a cube with same color sides on bottom, unaligned and checking initial to top rotation
    #Passing in a cube  same color sides and checking the count variable
    
    
    
    
    
    #Passing in no cube
    #Passing in an invalid cube
    
    def test_rotateController_001_rotate_ValidCubeLength(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbgwyrwybbboggrwwwrbrwwyryygooooborryoywbgwyyoggorgbr'
        inputDict['dir'] = 'R'
    
        expectedResult = {}
        expectedResult['status'] = 'error: Invalid Cube Length'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    def test_solve_010_ShouldReturnEmptyStringOnSolvedCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wwwwwwwwwgggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy'
    
        expectedResult = {}       
        expectedResult['cube'] = 'wwwwwwwwwgggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy'
        expectedResult['solution'] = ''
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        
    def test_solve_021_ShouldAlignDaisyAndSolveForBottomCross_OnInputCubeWithUnaignedBottomCross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yyogbbrbwbrryryrrwgogogrbowwbogoyogyogyoybgrybwgwwwbwr'
    
        expectedResult = {}       
        expectedResult['cube'] = 'borgbrobwyyggryorgwrbbgorgwwboyoyroyrbooyrygbgwbwwwgwy'
        expectedResult['solution'] = 'FFRRBBLLFFRRUBBUULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_030_ShouldAlignDaisyAndSolveForBottomCross_OnInputCubeWithDaisy(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ybbgborygwroyrgrrwwoorgbgowbgoyoyrbyywbwywgwrbryowbggo'
    
        expectedResult = {}       
        expectedResult['cube'] = 'borgbrobwyyggryorgwrbbgorgwwboyoyroyrbooyrygbgwbwwwgwy'
        expectedResult['solution'] = 'FFRRUBBUULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    # def test_solve_040_ShouldMoveBottomPiecesToTopDaisy(self):
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'ybogbgorgbbrwrywbwbowogyobrorrgooyrygwwyyrboyggrwwygwb'
    #
    #     expectedResult = {}       
    #     expectedResult['cube'] = 'booybgwrgyrrwrowbbyboggoobrwbryogyrobwbrywwwgggrywygoy'
    #     expectedResult['solution'] = 'LLUUBB'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    # def test_solve_041_ShouldMoveSidePiecesToTopDaisy(self):
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'ooyybgbyrrgowrggyygbbrgyrbwywgrobowworwryoybgrgwowobwb'
    #
    #     expectedResult = {}       
    #     expectedResult['cube'] = 'ygrobyoybwgogrrryywbrygrbbgywggobowybwbryorwggbwowowro'
    #     expectedResult['solution'] = 'BBf'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    # def test_solve_042_ShouldVerticalSidePiecesToTopDaisy(self):
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'grwbbbyowrryorwrgwgwoogyowybyooorggbyrobygwybrggywwrbb'
    #
    #     expectedResult = {}       
    #     expectedResult['cube'] = 'yrwrbbygbbbryrbrgggogrgboywogbooyrgbywywywoworywrwogow'
    #     expectedResult['solution'] = 'RRfrbRDBBUUr'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_043_ShouldSolveForBottomCrossGivenScrambledRubik(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'grwbbbyowrryorwrgwgwoogyowybyooorggbyrobygwybrggywwrbb'
    
        expectedResult = {}       
        expectedResult['cube'] = 'oybrbrybbygwbrorrgbgrbgbogwgggyoyrobyyoryoyoorwwwwwgww'
        expectedResult['solution'] = 'RRfrbRDBBUUrUFFUURRUUBBUULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    
    

        