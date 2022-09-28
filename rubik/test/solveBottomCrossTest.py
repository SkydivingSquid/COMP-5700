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
    #            dict['cube']:    string, valid cube
    #            dict['status']:    string: 'ok'
    #        abnormal:
    #            dict['status']: 'error: xxx', where xxx is a non-empty developer-selected diagnostic
    #
    #    confidence level:    boundary level analysis
    #    
    #    happy paths:
    #        (General single rotation instances)
    #        test 010: nominal valid cube with F rotation
    #        test 020: nominal valid cube with f rotation
    #        test 030: nominal valid cube with R rotation
    #        test 040: nominal valid cube with r rotation
    #        test 050: nominal valid cube with B rotation
    #        test 060: nominal valid cube with b rotation
    #        test 070: nominal valid cube with L rotation
    #        test 080: nominal valid cube with l rotation
    #        test 090: nominal valid cube with U rotation
    #        test 100: nominal valid cube with u rotation
    #        test 110: nominal valid cube with D rotation
    #        test 120: nominal valid cube with d rotation
    #
    #        (Unique rotation instances)
    #        test 130: nominal valid cube with missing rotation
    #        test 140: nominal valid cube with "" rotation
    #        test 150: nominal valid cube with missing 'dir' key
    #
    #        (Multiple rotation instance)
    #        test 160: nominal valid cube with multiple rotations.
    # 
    #    sad paths:
    #        (Cube class calls)
    #        test 610: Validate Cube class has been imported - checks for valid cube length
    #        test 620: validate Cube class has been imported - checks for valid cube chars
    #        test 630: Validate Cube class has been imported - checks for unique center cube colors
    #        test 640: Validate Cube class has been imported - checks for valid dir chars
    #        test 650: Abnormal Cube - Missing Cube Parameter
    #        test 660: Abnormal Cube class - checks for 9 of each color.
    #
    #    notes:
    #        The test for a valid cube with invalid rotation is tested in cubeTest. 
    #
    

    
    def test_solve_001_ValidCubeLength(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbgwyrwybbboggrwwwrbrwwyryygooooborryoywbgwyyoggorgbr'
        inputDict['dir'] = 'R'
    
        expectedResult = {}
        expectedResult['status'] = 'error: Invalid Cube Length'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    
    def test_rotateController_002_ValidCubeChars(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wbrbwwoyobryoroyrorobgZrbyrrrgyoyggyybgwbbowwgobwggwgw'
        inputDict['dir'] = ''
    
        expectedResult = {}
        expectedResult['status'] = 'error: Invalid Cube Char'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
     
    def test_rotateController_003_ValidCubeCenterChars(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wgbowogwrwbgbbrgrgoywbowrwrygwbygbyboryyggyrooybowwwoy'
        inputDict['dir'] = ''
    
        expectedResult = {}
        expectedResult['status'] = 'error: Duplicate Center Colors'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        
    def test_rotateController_004_CubeIsMissing(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'F'
    
        expectedResult = {}
        expectedResult['status'] = 'error: Missing Cube Argument'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotateController_005_rotate_CubeHasTooManyOfAColor(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'F'
        inputDict['cube'] = 'wwwwwwwwwwggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy'
    
        expectedResult = {}
        expectedResult['status'] = 'error: There May Only Be 9 Of Each Color'
    
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
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
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
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
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
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    # def test_solve_031_ShouldAlignDaisyAndSolveForBottomCross_OnInputCubeWithDaisy(self):
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'rrgboroyywoboyoobgrygygbwgobggrroyyrywowbwbwrwbbgwgwry'
    #
    #     expectedResult = {}       
    #     expectedResult['cube'] = 'bbgboyoorwyyoyroyrogbbgrgggrygorowryorwgbwygrbwwwwbywb'
    #     expectedResult['solution'] = 'UFFUUURRUBBUUUULL'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #     #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    # def test_solve_032_ShouldAlignDaisyAndSolveForBottomCross_OnInputCubeWithDaisy(self):
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'bogywbwwyrwwgbwbgyoggogowwbobygoogbryrrryrgrobbwyryryo'
    #
    #     expectedResult = {}       
    #     expectedResult['cube'] = ''
    #     expectedResult['solution'] = ''
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #     #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        
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
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
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
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_042_ShouldVerticalSidePiecesToTopDaisy(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rbogbgwwywrbyrbowrwgyogrbrgorybowoygboryywgybrbgowowgy'
    
        expectedResult = {}       
        expectedResult['cube'] = 'gyogbogbwbyrbrrorrgygygobgrwbygorworobyrygooywwbwwwbwy'
        expectedResult['solution'] = 'FURRfrFDRRUUUlUUUFFURRUUBBULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_043_ShouldSolveForBottomCrossGivenScrambledRubik(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bogywbwwyrwwgbwbgyoggogowwbobygoogbryrrryrgrobbwyryryo'
    
        expectedResult = {}       
        expectedResult['cube'] = 'rwgywogwbbwgwbgybyogwogbwgyobwgooborryyyyybbrorgrrrwro'
        expectedResult['solution'] = 'UFFURRUUBBULL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    
    
    
    
    
    
    
    
    #### CLASS TEST METHODS ####

    # def test_solve_900_ClassTestCaseValidatingBottomCheckWorks(self):
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'obrrooggobwryybboogworgbybgbwwyrwwgbrywgborogyyyrwrygw'
    #
    #     expectedResult = {}       
    #     expectedResult['cube'] = 'wywboyoobgbyoyrgyrogbbgrggyrygoroorrorwgbgrbywwywwwbwb'
    #     expectedResult['solution'] = 'FfrFDRRrbRDBBblBDLLUFFRRBBLL'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #     #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    #
    # def test_solve_901_ClassTestCaseValidatingHorizontalCheckWorks(self):
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'obrrooggobwryybboogworgbybgbwwyrwwgbrywgborogyyyrwrygw'
    #
    #     expectedResult = {}       
    #     expectedResult['cube'] = 'wywboyoobgbyoyrgyrogbbgrggyrygoroorrorwgbgrbywwywwwbwb'
    #     expectedResult['solution'] = 'FfrFDRRrbRDBBblBDLLUFFRRBBLL'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #     #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    #
    # def test_solve_902_ClassTestCaseValidatingHVerticalCheckWorks(self):
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'obrrooggobwryybboogworgbybgbwwyrwwgbrywgborogyyyrwrygw'
    #
    #     expectedResult = {}       
    #     expectedResult['cube'] = 'wywboyoobgbyoyrgyrogbbgrggyrygoroorrorwgbgrbywwywwwbwb'
    #     expectedResult['solution'] = 'FfrFDRRrbRDBBblBDLLUFFRRBBLL'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #     #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    #
    # #THIS IS A PROBLEM
    # def test_solve_990_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'wbgyoowrgyorbgbyyowrrgrybrobwywwgwwygbbrbgrwrogooyobyg'
    #
    #     expectedResult = {}       
    #     expectedResult['cube'] = 'grroorborybgbgwygborobrggrbwbbowwowrygygborwwwygyyywyo'
    #     expectedResult['solution'] = 'BBlrUUBUUFFUURRUUBBUULL'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #     #self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #
    def test_solve_991_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
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
    #
    def test_solve_992_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
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
    
    def test_solve_993_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
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
    
    def test_solve_994_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
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
    
    def test_solve_995_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
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
    
    def test_solve_996_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
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
    
    def test_solve_997_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
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
    
    def test_solve_998_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
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
    
    
    def test_solve_999_ShouldSolveExampleFromClass_ThoughInDifferentOrder(self):
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
    
    
    
    def test_solve_1000_RefactoredDaisyU(self):
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
    
    
    def test_solve_1001_RefactoredDaisyRot(self):
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
    
    
    def test_solve_1001_RefactoredDaisyU_Integrated(self):
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
    
    
    def test_solve_1010_RefactoredUnAlaignedBottomCubesToDaisyTop_Integrated(self):
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
    









        
        
        
    
    
    

        