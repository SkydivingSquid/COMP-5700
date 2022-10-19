'''
Created on Sep 25, 2022

@author: Martin
'''
import unittest
import rubik.solve as solve

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
    #        _2_ digit annotates test for Bottom Cross from iteration 2
    #        _3_ digit annotates test for Bottom Edges from iteration 3
    #
    #    happy paths:
    #        test 030: Find desired edge on nominal cube
    #        test 031: 
    #        test 032: 
    #        test 033: 
    #        test 034: 
    #        test 035: 
    #
    #        test 130: Return a solved bottom face from a solved cube
    #        test 131: Return a solved bottom face from cube with a incorrectly oriented edge (4)
    #        test 132: Return a solved bottom face from cube with a incorrectly oriented edge (3)
    #        test 133: Return a solved bottom face from cube with a incorrectly oriented edge (2)
    #        test 134: Return a solved bottom face from cube with a incorrectly oriented edge (1)
    #        test 135: Return a solved bottom face from cube with an out of place edge(4)
    #        test 136: Return a solved bottom face from cube with an out of place edge(3) 
    #        test 137: Return a solved bottom face from cube with an out of place edge(2)
    #        test 138: Return a solved bottom face from cube with an out of place edge(1)
    #        test 139: Return a solved bottom face from simple 'scramble'
    #        test 230: Return a solved bottom face from scrambled cube
    #
    #
    #    sad paths:
    #        (Cube class calls)
    #        test 010: Validate Cube class has been imported - checks for valid cube length
    #        test 011: validate Cube class has been imported - checks for valid cube chars
    #        test 012: Validate Cube class has been imported - checks for unique center cube colors
    #        test 013: Abnormal Cube - Missing Cube Parameter
    #        test 014: Abnormal Cube class - checks for 9 of each color.
    #
    

    
    def test_solve_010_ValidCubeLength(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbgwyrwybbboggrwwwrbrwwyryygooooborryoywbgwyyoggorgbr'
        inputDict['dir'] = 'R'
    
        expectedResult = {}
        expectedResult['status'] = 'error: Invalid Cube Length'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_rotateController_011_ValidCubeChars(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wbrbwwoyobryoroyrorobgZrbyrrrgyoyggyybgwbbowwgobwggwgw'
        inputDict['dir'] = ''
    
        expectedResult = {}
        expectedResult['status'] = 'error: Invalid Cube Char'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_rotateController_012_ValidCubeCenterChars(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wgbowogwrwbgbbrgrgoywbowrwrygwbygbyboryyggyrooybowwwoy'
        inputDict['dir'] = ''
    
        expectedResult = {}
        expectedResult['status'] = 'error: Duplicate Center Colors'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_rotateController_013_CubeIsMissing(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'F'
    
        expectedResult = {}
        expectedResult['status'] = 'error: Missing Cube Argument'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_rotateController_014_rotate_CubeHasTooManyOfAColor(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'F'
        inputDict['cube'] = 'wwwwwwwwwwggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy'
    
        expectedResult = {}
        expectedResult['status'] = 'error: There May Only Be 9 Of Each Color'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    
    
#ITERATION 3    
    
    def test_solve_031_FindCorrectBottomEdge(self):
        inputDict = {}
        inputDict['cube'] = 'wggrgwggwoyygyggygobbrbyrbywworwbrwrrwbrrbbyywoooooboy'
    
        expectedResult = 3
        actualResult = solve._findBottomEdge(inputDict['cube'], 49, 4, 13)
        self.assertEqual(actualResult, expectedResult)
    
    
    def test_032_rotationDirection(self):
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
    
    
    def test_033_orientCorrectTopEdgeIntoCorrectBottomEdge_v1(self):
        cube = 'obbbbbobbrrorrrrrrygyggggggrobooooobgygyyywyyywwwwwwww'
        solution = ''
        cubeLctn = 4
    
        expectedResult = {}
        expectedResult['solution'] = 'luuLUluLU'
        expectedResult['cube'] = list('yobybbbbbybrrrrrrrygrgggggggroooooooyybyyygbowwwwwwwww')
    
        actualResult = solve._topToBottomEdgeAlgorithm(cube,solution,cubeLctn, 1)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    
    def test_034_orientCorrectTopEdgeIntoCorrectBottomEdge_v1(self):
        cube = 'bobybbgbbybyrrrrrrrorggggggygwoorooobygyyyoboywwwwwwww'
        solution = ''
        cubeLctn = 4
    
        expectedResult = {}
        expectedResult['solution'] = 'luLU'
        expectedResult['cube'] = list('yobybbbbbybrrrrrrrygrgggggggroooooooyybyyygbowwwwwwwww')
    
        actualResult = solve._topToBottomEdgeAlgorithm(cube,solution,cubeLctn, 2)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    
    
    def test_035_solvingBottomEdgesMethod(self):
        cube = 'rrgybbbbboogrrrrrryooggggggwbboogooybbryyyyyyowwwwwwww'
        solution = ''
        cubeLctn = 1
    
        expectedResult = {}
        expectedResult['solution'] = 'u'
        expectedResult['cube'] = list('wbbybbbbbrrgrrrrrroogggggggyoooogooyryybyybyyowwwwwwww')
    
        actualResult = solve._solveBottomEdges(cube, solution, cubeLctn, 4)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solve_130_SolvingTheCubeToBottomFace_CompletedCube(self):
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
    
    def test_solve_131_SolvingTheCubeToBottomFace_F_L_P_E(self):
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
    
    def test_solve_132_SolvingTheCubeToBottomFace_F_L_R_E(self):
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
    
    def test_solve_133_SolvingTheCubeToBottomFace_B_L_L_E(self):
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
    
    def test_solve_134_SolvingTheCubeToBottomFace_B_L_R_E(self):
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
    
    
    def test_solve_135_SolvingTheCubeToBottomFace_MissplacedEdge4(self):
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
    
    
    def test_solve_136_SolvingTheCubeToBottomFace_MissplacedEdge3(self):
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
    
    def test_solve_137_SolvingTheCubeToBottomFace_MissplacedEdge2(self):
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
    
    def test_solve_138_SolvingTheCubeToBottomFace_MissplacedEdge1(self): #Tests the other U as well as edge1
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
    
    def test_solve_139_SolvingTheCubeToBottomFace_AllEdgesMissingSimpleRotationOut(self):
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
        
    def test_solve_230_SolvingTheCubeToBottomFace_ComplexScramble(self):
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
        
    
    
   
    
    
        
                                       