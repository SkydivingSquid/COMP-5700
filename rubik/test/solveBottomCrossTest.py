'''
Created on Sep 25, 2022

@author: Martin
'''
import unittest
import rubik.solve as solve
from unittest.case import expectedFailure


class solveBottomCrossTest(unittest.TestCase):
    
    
    # Analysis
    #    
    #    inputs:
    #        parms:    dict, mandatory, arrived validated
    #            parms['op']:    string: 'solve', mandatory, validated
    #            parms['cube']:    string: len=54, [brgoyw], 9 of each char, unique middle, mandatory, *Validated by Cube Class
    #
    #    outputs:
    #        side-effects:    non-state changes; no external effects (should not print anything)
    #        returns:    dict
    #        normal:
    #            dict['rotations']:    string, correct rotational solution
    #            dict['status']:    string: 'ok'
    #        abnormal:
    #            dict['status']: 'error: xxx', where xxx is a non-empty developer-selected diagnostic
    #
    #    assumptions:     the given input cube, assuming all other validity checks pass, will be of 'possible' combinations. 
    #
    #    confidence level:    boundary level analysis, minus impossible-cube orientation checks (graduates)
    #    
    #    test path notes:
    #        _1_ digit annotates test for input verification from iteration 1
    #        _2_ digit annotates test for Bottom Cube from iteration 2
    #        R2_ digit annotates test for manual refactoring
    #
    #    happy paths:

    #        test 020: Input nominal cube with bottom cross already solved
    #        test 021: Input nominal cube with unaligned bottom cross
    #        test 022: Input nominal cube with daisy solved
    #        test 023: Input nominal cube with unaligned daisy
    #        test 024: Input nominal cube with neither bottom cross nor daisy
    
    #        test R20: Input nominal cube list checking for U rotation
    #        test R21: Input nominal cube list checking for directional rotations
    #        test R23: Input nominal cube list with simple solution checking for integrated U and directional rotations
    #        test R22: Input nominal cube list checking for integrated U and directional rotations
    
    #        test 030: Find desired edge on nominal cube
     
    #        test 620: Scrambled Cube
    #        test 621: Scrambled Cube
    #        test 622: Scrambled Cube
    #        test 623: Scrambled Cube
    #        test 624: Scrambled Cube
    #        test 625: Scrambled Cube
    #        test 626: Scrambled Cube
    #        test 627: Scrambled Cube
    #        test 628: Scrambled Cube
    #        test 629: Scrambled Cube
    #       
    #    sad paths:
    #        (Cube class calls)
    #        test 010: Validate Cube class has been imported - checks for valid cube length
    #        test 011: validate Cube class has been imported - checks for valid cube chars
    #        test 012: Validate Cube class has been imported - checks for unique center cube colors
    #        test 013: Abnormal Cube - Missing Cube Parameter
    #        test 014: Abnormal Cube class - checks for 9 of each color.
    #
    

    
    # def test_solve_010_ValidCubeLength(self):
    #     inputDict = {}
    #     inputDict['op'] = 'rotate'
    #     inputDict['cube'] = 'bbgwyrwybbboggrwwwrbrwwyryygooooborryoywbgwyyoggorgbr'
    #     inputDict['dir'] = 'R'
    #
    #     expectedResult = {}
    #     expectedResult['status'] = 'error: Invalid Cube Length'
    #
    #     actualResult = solve._solve(inputDict)
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    # def test_rotateController_011_ValidCubeChars(self):
    #     inputDict = {}
    #     inputDict['op'] = 'rotate'
    #     inputDict['cube'] = 'wbrbwwoyobryoroyrorobgZrbyrrrgyoyggyybgwbbowwgobwggwgw'
    #     inputDict['dir'] = ''
    #
    #     expectedResult = {}
    #     expectedResult['status'] = 'error: Invalid Cube Char'
    #
    #     actualResult = solve._solve(inputDict)
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    # def test_rotateController_012_ValidCubeCenterChars(self):
    #     inputDict = {}
    #     inputDict['op'] = 'rotate'
    #     inputDict['cube'] = 'wgbowogwrwbgbbrgrgoywbowrwrygwbygbyboryyggyrooybowwwoy'
    #     inputDict['dir'] = ''
    #
    #     expectedResult = {}
    #     expectedResult['status'] = 'error: Duplicate Center Colors'
    #
    #     actualResult = solve._solve(inputDict)
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    # def test_rotateController_013_CubeIsMissing(self):
    #     inputDict = {}
    #     inputDict['op'] = 'rotate'
    #     inputDict['dir'] = 'F'
    #
    #     expectedResult = {}
    #     expectedResult['status'] = 'error: Missing Cube Argument'
    #
    #     actualResult = solve._solve(inputDict)
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    # def test_rotateController_014_rotate_CubeHasTooManyOfAColor(self):
    #     inputDict = {}
    #     inputDict['op'] = 'rotate'
    #     inputDict['dir'] = 'F'
    #     inputDict['cube'] = 'wwwwwwwwwwggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy'
    #
    #     expectedResult = {}
    #     expectedResult['status'] = 'error: There May Only Be 9 Of Each Color'
    #
    #     actualResult = solve._solve(inputDict)
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    #
    # def test_solve_R20_RefactoredDaisyU(self):
    #     inputList = ['r', 'r', 'g', 'b', 'o', 'r', 'o', 'y', 'y', 
    #                  'w', 'o', 'b', 'o', 'y', 'o', 'o', 'b', 'g', 
    #                  'r', 'y', 'g', 'y', 'g', 'b', 'w', 'g', 'o', 
    #                  'b', 'g', 'g', 'r', 'r', 'o', 'y', 'y', 'r', 
    #                  'y', 'w', 'o', 'w', 'b', 'w', 'b', 'w', 'r', 
    #                  'w', 'b', 'b', 'g', 'w', 'g', 'w', 'r', 'y']
    #
    #     solution = ""
    #
    #     expectedResult = {}
    #     expectedResult['list'] = ['w', 'o', 'b', 'b', 'o', 'r', 'o', 'y', 'y', 
    #                              'r', 'y', 'g', 'o', 'y', 'o', 'o', 'b', 'g', 
    #                              'b', 'g', 'g', 'y', 'g', 'b', 'w', 'g', 'o', 
    #                              'r', 'r', 'g', 'r', 'r', 'o', 'y', 'y', 'r', 
    #                              'b', 'w', 'y', 'w', 'b', 'w', 'r', 'w', 'o', 
    #                              'w', 'b', 'b', 'g', 'w', 'g', 'w', 'r', 'y']
    #
    #     expectedResult['solution'] = 'U'
    #
    #
    #     actualResult = solve._daisyURotations(4, 1, 43, inputList, solution)
    #
    #     self.assertEqual(expectedResult.get('list'), actualResult.get('daisyCubeList'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    #
    # def test_solve_R21_RefactoredDaisyRot(self):
    #     inputList = ['w', 'o', 'b', 'b', 'o', 'r', 'o', 'y', 'y', 
    #                  'r', 'y', 'g', 'o', 'y', 'o', 'o', 'b', 'g', 
    #                  'b', 'g', 'g', 'y', 'g', 'b', 'w', 'g', 'o', 
    #                  'r', 'r', 'g', 'r', 'r', 'o', 'y', 'y', 'r', 
    #                  'b', 'w', 'y', 'w', 'b', 'w', 'r', 'w', 'o', 
    #                  'w', 'b', 'b', 'g', 'w', 'g', 'w', 'r', 'y']
    #
    #     solution = ""
    #
    #     expectedResult = {}
    #     expectedResult['list'] = ['y', 'y', 'o', 'r', 'o', 'b', 'b', 'o', 'w', 
    #                               'r', 'y', 'g', 'o', 'y', 'o', 'g', 'b', 'g', 
    #                               'b', 'g', 'g', 'y', 'g', 'b', 'w', 'g', 'o', 
    #                               'r', 'r', 'o', 'r', 'r', 'o', 'y', 'y', 'r', 
    #                               'b', 'w', 'y', 'w', 'b', 'w', 'b', 'b', 'w', 
    #                               'o', 'w', 'r', 'g', 'w', 'g', 'w', 'r', 'y']
    #
    #     expectedResult['solution'] = 'FF'
    #
    #
    #     actualResult = solve._daisy_Rotations(4, 1, inputList, solution)
    #
    #     self.assertEqual(expectedResult.get('list'), actualResult.get('daisyCubeList'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    #
    # def test_solve_R22_RefactoredDaisyU_Integrated(self):
    #
    #     inputList = ['r', 'r', 'g', 'b', 'o', 'r', 'o', 'y', 'y', 
    #                  'w', 'o', 'b', 'o', 'y', 'o', 'o', 'b', 'g', 
    #                  'r', 'y', 'g', 'y', 'g', 'b', 'w', 'g', 'o', 
    #                  'b', 'g', 'g', 'r', 'r', 'o', 'y', 'y', 'r', 
    #                  'y', 'w', 'o', 'w', 'b', 'w', 'b', 'w', 'r', 
    #                  'w', 'b', 'b', 'g', 'w', 'g', 'w', 'r', 'y']
    #
    #     solution = ""
    #
    #     expectedResult = {}
    #     expectedResult['list'] = ['y', 'y', 'o', 'r', 'o', 'b', 'b', 'o', 'w', 
    #                               'r', 'y', 'g', 'o', 'y', 'o', 'g', 'b', 'g', 
    #                               'b', 'g', 'g', 'y', 'g', 'b', 'w', 'g', 'o', 
    #                               'r', 'r', 'o', 'r', 'r', 'o', 'y', 'y', 'r', 
    #                               'b', 'w', 'y', 'w', 'b', 'w', 'b', 'b', 'w', 
    #                               'o', 'w', 'r', 'g', 'w', 'g', 'w', 'r', 'y']
    #
    #     expectedResult['solution'] = 'UFF'
    #
    #
    #     actualResult = solve._daisyIntegrated(4, 1, 43, inputList, solution)
    #
    #     self.assertEqual(expectedResult.get('list'), actualResult.get('daisyCubeList'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    #
    # def test_solve_R23_RefactoredUnAlaignedBottomCubesToDaisyTop_Integrated(self):
    #
    #     inputList = ['o', 'r', 'g', 'o', 'b', 'w', 'b', 'w', 'w', 
    #                  'o', 'y', 'o', 'b', 'r', 'o', 'b', 'b', 'g', 
    #                  'w', 'o', 'y', 'w', 'y', 'r', 'b', 'r', 'w', 
    #                  'r', 'o', 'b', 'b', 'o', 'y', 'y', 'y', 'r', 
    #                  'g', 'b', 'y', 'g', 'w', 'g', 'g', 'g', 'y', 
    #                  'w', 'y', 'o', 'r', 'g', 'g', 'r', 'w', 'r']
    #
    #     solution = "bFFlfLDFFU"
    #
    #     expectedResult = {}
    #     expectedResult['list'] = ['o', 'y', 'b', 'o', 'b', 'w', 'b', 'w', 'r', 
    #                               'g', 'b', 'b', 'o', 'r', 'b', 'y', 'o', 'w', 
    #                               'w', 'o', 'b', 'w', 'y', 'r', 'o', 'r', 'w', 
    #                               'o', 'r', 'g', 'b', 'o', 'y', 'y', 'y', 'r', 
    #                               'g', 'g', 'o', 'g', 'w', 'g', 'y', 'g', 'r', 
    #                               'w', 'y', 'g', 'r', 'g', 'b', 'r', 'w', 'y']
    #
    #     expectedResult['solution'] = 'bFFlfLDFFUURR'
    #
    #
    #     actualResult = solve._unalignedBottomToDaisy(50, 41, solution, inputList) 
    #
    #     self.assertEqual(expectedResult.get('list'), actualResult.get('rotatedCubeList'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    #
    #
    #
    #
    #
    #
    #
    #
    
    def test_solve_0300_SolvingTheCubeToBottomFace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
    
        expectedResult = {}
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        expectedResult['solution'] = ''
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    
    
    def test_solve_0302_SolvingTheCubeToBottomFace_F_L_P_E(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'obbybbwbbrrgrrrrrryooggggggygyooooobgbryyybyyowwwwwwww'
    
        expectedResult = {}
        expectedResult['cube'] = list('yobybbbbbybrrrrrrrygrgggggggroooooooyybyyygbowwwwwwwww')
        expectedResult['solution'] = 'luLUluuLUluLU'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_0303_SolvingTheCubeToBottomFace_F_L_R_E(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yoybbbbbrbrryrrwrrggoggggggybboooooogyyryyoyrwwbwwwwww'
    
        expectedResult = {}
        expectedResult['cube'] = list('ogbbbbbbbybryrrrrryrgggggggyogoooooorybyyryyowwwwwwwww')
        expectedResult['solution'] = 'fuFUfuuFUfuFU' 
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_0304_SolvingTheCubeToBottomFace_B_L_L_E(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yrrbbbbbbybyrrrrrgrggyggwggoobooooooyygyyyogbwwwwwwwwr'
    
        expectedResult = {}
        expectedResult['cube'] = list('ybobbbbbbborrrrrrryrgygggggygooooooorgbyyygyywwwwwwwww')
        expectedResult['solution'] = 'ruRUruuRUruRU' 
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        #self.assertTrue(actualResult)
    
    def test_solve_0305_SolvingTheCubeToBottomFace_B_L_R_E(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbrbbbbbbyggrrrrrryrygggggogooyoowoooyryyoyybwwwwwwgww'
    
        expectedResult = {}
        expectedResult['cube'] = list('yobbbbbbbyrbrrrrrrrbgggggggygoyoooooryyoyygyowwwwwwwww')
        expectedResult['solution'] = 'buBUbuuBUbuBU' 
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    
    def test_solve_0306_SolvingTheCubeToBottomFace_MissplacedEdge4(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrgybbbbboogrrrrrryooggggggwbboogooybbryyyyyyowwwwwwww'
    
        expectedResult = {}
        expectedResult['cube'] = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        expectedResult['solution'] = 'uulUL' 
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    
    def test_solve_0307_SolvingTheCubeToBottomFace_MissplacedEdge3(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wrrbbobbyggoyrrrrrbboggggggybboooooogyyryyryywwbwwwwww'
    
        expectedResult = {}
        expectedResult['cube'] = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        expectedResult['solution'] = 'uufUF' 
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_0308_SolvingTheCubeToBottomFace_MissplacedEdge2(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rwwbbbbbboggwwbwwryybrgggggwwbyyyyyyrrrrrryggoooooooow'
    
        expectedResult = {}
        expectedResult['cube'] = list('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww')
        expectedResult['solution'] = 'uurUR' 
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_0309_SolvingTheCubeToBottomFace_MissplacedEdge1(self): #Tests the other U as well as edge1
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oyybbbbbbbbwwwwwwwggwggwggrrggryyyyybrryrryrroooooogoo'
    
        expectedResult = {}
        expectedResult['cube'] = list('bbbbbbbbbwwwwwwwwwgggggggggyyyyyyyyyrrrrrrrrrooooooooo')
        expectedResult['solution'] = 'UubUB' 
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_0310_SolvingTheCubeToBottomFace_AllEdgesMissingSimpleRotationOut(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'obbybobbowrrbrbbrbwggygrygroowyogyoyyogyyggrrowwwwwgwr'
    
        expectedResult = {}
        expectedResult['cube'] = list('bbbbbbbbbwwwwwwwwwgggggggggyyyyyyyyyrrrrrrrrrooooooooo')
        expectedResult['solution'] = 'ufUFurURubUBulUL' 
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_0311_SolvingTheCubeToBottomFace_ComplexScramble(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbwgobryyoowwwobbggrywrwrgrgwwryywoyobrgbgoygbroygobry'
    
        expectedResult = {}
        expectedResult['cube'] = list('yyooorooowbybwbwwwoowyrorrrrrrbywyyybybwbwbrbggggggggg')
        expectedResult['solution'] = 'UlUUUBBrbRDBBUFFURRUUBBULLfuFUfuuFUfuFUruRUruuRUruRUUUbuuBUbuBUUUulUL' 
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    

    
    def test_solve_031_FindCorrectBottomEdge(self):
        inputDict = {}
        inputDict['cube'] = 'wggrgwggwoyygyggygobbrbyrbywworwbrwrrwbrrbbyywoooooboy'
    
        expectedResult = 3
        actualResult = solve._findBottomEdge(inputDict['cube'], 49, 4, 13)
        self.assertEqual(actualResult, expectedResult)
    
    def test_solve_032_SolveBottomFace2(self):
        cube  = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        solution = 'QQQ'
        expectedResult  = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', 'QQQ'
        actualResult = solve._solveBottomFace(cube, solution)
        self.assertTrue(actualResult)
    
    
    def test_998_rotationDirection(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        solution = {}
        solution['solution'] = 'abc'
        letter = 'f'
    
        expectedResult = {}
        expectedResult['solution'] = 'abcf'
        expectedResult['cube'] = 'bbbbbbbbbwrrwrrwrrgggggggggooyooyooyyyyyyyrrrooowwwwww'
    
        actualResult = {}
    
        actualResult['solution'], actualResult['cube'] = solve._functionalRotations(cube, solution, letter)
    
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    
    
    def test_997_orientCorrectTopEdgeIntoCorrectBottomEdge(self):
        cube = 'obbbbbobbrrorrrrrrygyggggggrobooooobgygyyywyyywwwwwwww'
        #This Cube has Bottom Center Color at index[2]
        solution = ''
        cubeLctn = 4
    
        expectedResult = {}
        expectedResult['solution'] = 'luuLUluLU'
        expectedResult['cube'] = list('yobybbbbbybrrrrrrrygrgggggggroooooooyybyyygbowwwwwwwww')
    
        actualResult = solve._topToBottomEdgeAlgorithm(cube,solution,cubeLctn, 1)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    
    def test_996_orientCorrectTopEdgeIntoCorrectBottomEdge(self):
        cube = 'bobybbgbbybyrrrrrrrorggggggygwoorooobygyyyoboywwwwwwww'
        #This Cube has Bottom Center Color at index[2]
        solution = ''
        cubeLctn = 4
    
        expectedResult = {}
        expectedResult['solution'] = 'luLU'
        expectedResult['cube'] = list('yobybbbbbybrrrrrrrygrgggggggroooooooyybyyygbowwwwwwwww')
    
        actualResult = solve._topToBottomEdgeAlgorithm(cube,solution,cubeLctn, 2)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    
    
    def test_995_solvingBottomEdgesMethod(self):
        cube = 'rrgybbbbboogrrrrrryooggggggwbboogooybbryyyyyyowwwwwwww'
        solution = ''
        cubeLctn = 1
    
        expectedResult = {}
        expectedResult['solution'] = 'u'
        expectedResult['cube'] = list('wbbybbbbbrrgrrrrrroogggggggyoooogooyryybyybyyowwwwwwww')
    
        actualResult = solve._solveBottomEdges(cube, solution, cubeLctn, 4)
    
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    
    
   
    
    
        
                                       