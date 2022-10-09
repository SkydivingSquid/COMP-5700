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

    def test_solve_020_ShouldReturnEmptyStringOnSolvedCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wwwwwwwwwgggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy'
    
        expectedResult = {}       
        expectedResult['cube'] = 'wwwwwwwwwgggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy'
        expectedResult['solution'] = ''
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
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
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_022_ShouldAlignDaisyAndSolveForBottomCross_OnInputCubeWithDaisy(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ybbgborygwroyrgrrwwoorgbgowbgoyoyrbyywbwywgwrbryowbggo'
    
        expectedResult = {}       
        expectedResult['cube'] = 'borgbrobwyyggryorgwrbbgorgwwboyoyroyrbooyrygbgwbwwwgwy'
        expectedResult['solution'] = 'FFRRUBBUULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_023_ShouldMoveVerticalSidePiecesToTopDaisy(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rbogbgwwywrbyrbowrwgyogrbrgorybowoygboryywgybrbgowowgy'
    
        expectedResult = {}       
        expectedResult['cube'] = 'gyogbogbwbyrbrrorrgygygobgrwbygorworobyrygooywwbwwwbwy'
        expectedResult['solution'] = 'FURRfrFDRRUUUlUUUFFURRUUBBULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_024_ShouldSolveForBottomCrossGivenScrambledRubik(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bogywbwwyrwwgbwbgyoggogowwbobygoogbryrrryrgrobbwyryryo'
    
        expectedResult = {}       
        expectedResult['cube'] = 'rwgywogwbbwgwbgybyogwogbwgyobwgooborryyyyybbrorgrrrwro'
        expectedResult['solution'] = 'UFFURRUUBBULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
    def test_solve_R20_RefactoredDaisyU(self):
        inputList = ['r', 'r', 'g', 'b', 'o', 'r', 'o', 'y', 'y', 
                     'w', 'o', 'b', 'o', 'y', 'o', 'o', 'b', 'g', 
                     'r', 'y', 'g', 'y', 'g', 'b', 'w', 'g', 'o', 
                     'b', 'g', 'g', 'r', 'r', 'o', 'y', 'y', 'r', 
                     'y', 'w', 'o', 'w', 'b', 'w', 'b', 'w', 'r', 
                     'w', 'b', 'b', 'g', 'w', 'g', 'w', 'r', 'y']
    
        solution = ""
    
        expectedResult = {}
        expectedResult['list'] = ['w', 'o', 'b', 'b', 'o', 'r', 'o', 'y', 'y', 
                                 'r', 'y', 'g', 'o', 'y', 'o', 'o', 'b', 'g', 
                                 'b', 'g', 'g', 'y', 'g', 'b', 'w', 'g', 'o', 
                                 'r', 'r', 'g', 'r', 'r', 'o', 'y', 'y', 'r', 
                                 'b', 'w', 'y', 'w', 'b', 'w', 'r', 'w', 'o', 
                                 'w', 'b', 'b', 'g', 'w', 'g', 'w', 'r', 'y']
    
        expectedResult['solution'] = 'U'
    
    
        actualResult = solve._daisyURotations(4, 1, 43, inputList, solution)
    
        self.assertEqual(expectedResult.get('list'), actualResult.get('daisyCubeList'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    
    def test_solve_R21_RefactoredDaisyRot(self):
        inputList = ['w', 'o', 'b', 'b', 'o', 'r', 'o', 'y', 'y', 
                     'r', 'y', 'g', 'o', 'y', 'o', 'o', 'b', 'g', 
                     'b', 'g', 'g', 'y', 'g', 'b', 'w', 'g', 'o', 
                     'r', 'r', 'g', 'r', 'r', 'o', 'y', 'y', 'r', 
                     'b', 'w', 'y', 'w', 'b', 'w', 'r', 'w', 'o', 
                     'w', 'b', 'b', 'g', 'w', 'g', 'w', 'r', 'y']
    
        solution = ""
    
        expectedResult = {}
        expectedResult['list'] = ['y', 'y', 'o', 'r', 'o', 'b', 'b', 'o', 'w', 
                                  'r', 'y', 'g', 'o', 'y', 'o', 'g', 'b', 'g', 
                                  'b', 'g', 'g', 'y', 'g', 'b', 'w', 'g', 'o', 
                                  'r', 'r', 'o', 'r', 'r', 'o', 'y', 'y', 'r', 
                                  'b', 'w', 'y', 'w', 'b', 'w', 'b', 'b', 'w', 
                                  'o', 'w', 'r', 'g', 'w', 'g', 'w', 'r', 'y']
    
        expectedResult['solution'] = 'FF'
    
    
        actualResult = solve._daisy_Rotations(4, 1, inputList, solution)
    
        self.assertEqual(expectedResult.get('list'), actualResult.get('daisyCubeList'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    
    def test_solve_R22_RefactoredDaisyU_Integrated(self):

        inputList = ['r', 'r', 'g', 'b', 'o', 'r', 'o', 'y', 'y', 
                     'w', 'o', 'b', 'o', 'y', 'o', 'o', 'b', 'g', 
                     'r', 'y', 'g', 'y', 'g', 'b', 'w', 'g', 'o', 
                     'b', 'g', 'g', 'r', 'r', 'o', 'y', 'y', 'r', 
                     'y', 'w', 'o', 'w', 'b', 'w', 'b', 'w', 'r', 
                     'w', 'b', 'b', 'g', 'w', 'g', 'w', 'r', 'y']
    
        solution = ""
    
        expectedResult = {}
        expectedResult['list'] = ['y', 'y', 'o', 'r', 'o', 'b', 'b', 'o', 'w', 
                                  'r', 'y', 'g', 'o', 'y', 'o', 'g', 'b', 'g', 
                                  'b', 'g', 'g', 'y', 'g', 'b', 'w', 'g', 'o', 
                                  'r', 'r', 'o', 'r', 'r', 'o', 'y', 'y', 'r', 
                                  'b', 'w', 'y', 'w', 'b', 'w', 'b', 'b', 'w', 
                                  'o', 'w', 'r', 'g', 'w', 'g', 'w', 'r', 'y']
    
        expectedResult['solution'] = 'UFF'
    
    
        actualResult = solve._daisyIntegrated(4, 1, 43, inputList, solution)
    
        self.assertEqual(expectedResult.get('list'), actualResult.get('daisyCubeList'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        
    def test_solve_R23_RefactoredUnAlaignedBottomCubesToDaisyTop_Integrated(self):

        inputList = ['o', 'r', 'g', 'o', 'b', 'w', 'b', 'w', 'w', 
                     'o', 'y', 'o', 'b', 'r', 'o', 'b', 'b', 'g', 
                     'w', 'o', 'y', 'w', 'y', 'r', 'b', 'r', 'w', 
                     'r', 'o', 'b', 'b', 'o', 'y', 'y', 'y', 'r', 
                     'g', 'b', 'y', 'g', 'w', 'g', 'g', 'g', 'y', 
                     'w', 'y', 'o', 'r', 'g', 'g', 'r', 'w', 'r']
    
        solution = "bFFlfLDFFU"
    
        expectedResult = {}
        expectedResult['list'] = ['o', 'y', 'b', 'o', 'b', 'w', 'b', 'w', 'r', 
                                  'g', 'b', 'b', 'o', 'r', 'b', 'y', 'o', 'w', 
                                  'w', 'o', 'b', 'w', 'y', 'r', 'o', 'r', 'w', 
                                  'o', 'r', 'g', 'b', 'o', 'y', 'y', 'y', 'r', 
                                  'g', 'g', 'o', 'g', 'w', 'g', 'y', 'g', 'r', 
                                  'w', 'y', 'g', 'r', 'g', 'b', 'r', 'w', 'y']
    
        expectedResult['solution'] = 'bFFlfLDFFUURR'
    
    
        actualResult = solve._unalignedBottomToDaisy(50, 41, solution, inputList) 
    
        self.assertEqual(expectedResult.get('list'), actualResult.get('rotatedCubeList'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        
        
    
    def test_solve_620_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):  
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wbgyoowrgyorbgbyyowrrgrybrobwywwgwwygbbrbgrwrogooyobyg'
    
        expectedResult = {}       
        expectedResult['cube'] = 'grroorborybgbgwygborobrggrbwbbowwowrygygborwwwygyyywyo'
        expectedResult['solution'] = 'BBlrUUBUUFFUURRUUBBUULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_621_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bobwbwggworrbrrbrgywoyyybroyowgoyygygowbwgrygroobgwwbr'
    
        expectedResult = {}       
        expectedResult['cube'] = 'goyobwbbowrbbrbgrrowbrywyywwybooyooroygrwwrbrwgygggygg'
        expectedResult['solution'] = 'bFFlfLDFFUURRUFFURRBBULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_622_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wooyggyorrwobryggobrywoobgrooyrybwbgwgrbbrgywbwbrwwgyy'
    
        expectedResult = {}       
        expectedResult['cube'] = 'obwoggggyrgbrrrbroggrooowoyobbyybwyybbrrbyyygwwgwwwowr'
        expectedResult['solution'] = 'FFRRURUUfUUFFURRBBULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_623_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oggyobbygybywwoybbrywyrwgwwrbbogryggbwwgbowooogrryrorr'
    
        expectedResult = {}       
        expectedResult['cube'] = 'ywygowoowgrbbwbbwwrgbrroyrboowbgooggwbgwbgrrryyryyygyo'
        expectedResult['solution'] = 'lrFFlfLDFFrbRDBBUFFRRBBLL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_624_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbyywwoobwrwrooyggywowgbygrggoyywogwbbrrbywobrrgorbgyr'
    
        expectedResult = {}       
        expectedResult['cube'] = 'ogybwbbwrbobwoygooyyybgbbgrrgrgyooywwwwobwwygoryrrrgrg'
        expectedResult['solution'] = 'FFUFRFFUURRUUBBUULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_625_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ygoywyywrrgowbogrbwroggbgywyrgrobbwwgwyoyybbwbboorgror'
    
        expectedResult = {}       
        expectedResult['cube'] = 'rwgywogwbbwgwbgybyogwogbwgyobwgooborryyyyybbrorgrrrwro'
        expectedResult['solution'] = 'bRRfrFDRRblBDLLUUUrUFFURRUUBBULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_626_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wbwbroybygroyywroryorgbrgrbwrgwggowwybbyoorybbwoywgggo'
    
        expectedResult = {}       
        expectedResult['cube'] = 'bogrrrwrywbrgyrryowooybbgbygogggoogbryygoywbrywowwwbwb'
        expectedResult['solution'] = 'FFBLLblBDLLUFFlfLDFFFFURRBBULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_627_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yogrwbbwowwoyrorbwryobboyrybbwggwbwrggbgogrroyywoyrgyg'
    
        expectedResult = {}       
        expectedResult['cube'] = 'ywoowbrwgrorgrobrgyrobbwwbrgrbggrygowwbboggobwyoyyywyy'
        expectedResult['solution'] = 'FFBBUFBBrbRDBBUUUFFURRUUBBULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_628_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yrrwrwyggoybybrorygbbyggwwyogbwwogybroobobgowrowgybwrr'
    
        expectedResult = {}       
        expectedResult['cube'] = 'brwbrbrrboworbgybrrogbgrwgyywowwobwwwgbgoogogyyryyygyo'
        expectedResult['solution'] = 'frLLblBDLLUUfUUUFFRRBBLL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_629_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'obrrooggobwryybboogworgbybgbwwyrwwgbrywgborogyyyrwrygw'
    
        expectedResult = {}       
        expectedResult['cube'] = 'wywboyoobgbyoyrgyrogbbgrggyrygoroorrorwgbgrbywwywwwbwb'
        expectedResult['solution'] = 'FfrFDRRrbRDBBblBDLLUFFRRBBLL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_030_SolveBottomFace(self):
        cube  = 'wggrgwggwoyygyggygobbrbyrbywworwbrwrrwbrrbbyywoooooboy'
        
        #expectedResult = 3
        expectedResult = 'wggrgwggwoyygyggygobbrbyrbywworwbrwrrwbrrbbyywoooooboy'
        actualResult = solve._solveBottomFace(cube)
        self.assertEqual(actualResult, expectedResult)
        
        
    def test_solve_031_FindCorrectBottomEdge(self):
        inputDict = {}
        inputDict['cube'] = 'wggrgwggwoyygyggygobbrbyrbywworwbrwrrwbrrbbyywoooooboy'
        
        expectedResult = 3
        actualResult = solve._findBottomEdge(inputDict['cube'], 49, 4, 13)
        self.assertEqual(actualResult, expectedResult)
        
    def test_solve_032_SolveBottomFace2(self):
        cube  = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        expectedResult  = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBottomFace(cube)
        self.assertTrue(actualResult)
        
    def test_solve_033_SolveBottomEdges(self):
        cube = 'ybbbbobbywrryrrrrrggoggggggbboooooooyyyyyygrrwwbwwwwww'
        solution = ""
        cubeLocation = 3
        
        expectedResult = cube, solution
        actualResult = solve._solveBottomEdges(cube, solution, cubeLocation)
        self.assertEqual(expectedResult, actualResult)

    def test_solve_034_movingBottomEdgeToTopEdge(self):
        cube = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
        solution = {}
        solution['solution'] = 'fuFU'
        value = 7
    
        expectedResult = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'w', 'r', 'r', 'w', 'r', 'r', 'w', 'r', 'r', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'o', 'o', 'y', 'o', 'o', 'y', 'o', 'o', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'r', 'r', 'r', 'o', 'o', 'o', 'w', 'w', 'w', 'w', 'w', 'w'], 'f',2
        actualResult = solve._moveBottomEdgeToTopEdge(cube, solution, value)
        self.assertEqual(expectedResult,actualResult)
        
        
        
        #Needs specific type of cube, and specific type of solution (ie result)
    def test_999_functionalMovement(self):
        
        cube = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
        solution = {}
        solution['solution'] = '' 
        letter = 'f'
        
        expectedResult = 'f', ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'w', 'r', 'r', 'w', 'r', 'r', 'w', 'r', 'r', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'o', 'o', 'y', 'o', 'o', 'y', 'o', 'o', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'r', 'r', 'r', 'o', 'o', 'o', 'w', 'w', 'w', 'w', 'w', 'w']
        actualResult = solve._functionalRotations(cube, solution, letter)
        self.assertEqual(expectedResult, actualResult)
                                             
                                             
                                       