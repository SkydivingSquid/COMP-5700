'''
Created on Oct 19, 2022

@author: Martin
'''
import unittest
import rubik.solve as solve

class solveMiddleLayerTest(unittest.TestCase):
        
    def test_solve_040_FindCorrectMiddleEdge(self):
        cube = 'rybobbbbbyygrrrrrryboggbgggyybyogooogoroyrygowwwwwwwww'
    
        expectedResult = 8
        actualResult = solve._findMiddleEdge(cube, 22, 31)
        self.assertEqual(actualResult, expectedResult)

    def test_solve_041_MoveMiddleEdgeToTopSide(self):
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
        
    def test_solve_042_topToMiddleEdgeAlgorithm(self):
        cube = 'gygrbbbbbyybrrrrrrrooggbgggboyyoyoooygybyoogrwwwwwwwww'
        solution = ''
        cubeLocation = 3
        colorMarker = 1
        
        expectedResult = {}
        expectedResult['cube'] = list('gobrbbbbbybyrrrrrrgybggggggrorooyoooygobyyyyowwwwwwwww')
        expectedResult['solution'] = 'uubUBULul'
        
        actualResult= solve._topToMiddleEdgeAlgorithm(cube, solution, cubeLocation, colorMarker)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    
    def test_solve_043_unalighedMiddleEdge(self):
        cube = 'oyyobrbbbggbbryrrrrbyggbgggryyyogooogoyryrboowwwwwwwww'
        solution = '' 
        result = {}
        cubeLctn =  5
        initialEdge = 1
        markerEdge1 = 43
        markerEdge2 = 1 
        center = 4
        sideEdge1 = 13
        sideEdge2 = 2
    
        expectedResult = {}
        expectedResult['cube'] = list('bbbobbbbbyyyrryrrrgogggbgggygyyogoooryoryrroowwwwwwwww')
        expectedResult['solution'] = 'URurufUFUUURurufUF'
    
        actualResult = {}
        actualResult['cubeLctn'], actualResult['cube'], actualResult['solution'] = solve._unalighedMiddleEdge(cube, solution, result, cubeLctn, initialEdge, markerEdge1, markerEdge2, center, sideEdge1, sideEdge2)
    
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    
    def test_solve_046_solveMiddleLayer(self):
        cube = 'yyooorooowbybwbwwwoowyrorrrrrrbywyyybybwbwbrbggggggggg'
        solution = ''
    
        expectedResult = {}
        expectedResult['cube'] = list('yoooooooowwrwwwwwwbbrrrrrrrybbyyyyyybrwybbobbggggggggg')
        expectedResult['solution'] = 'uFufulULUURurufUFuuurURUBubuubUBULulUFufulUL'
        
        actualResult= solve._solveMiddleLayer(cube, solution)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    
    
    def test_solve_046_SolvingTheMiddleLayer_ComplexScramble(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ybwrbgoyyowgwrybwroowogggwbrggyobygwbbyryrrygbroowbrow'
    
        expectedResult = {}
        expectedResult['cube'] = list('gbybbbbbbgryrrrrrrbyyggggggoyrooooooborgyyyyowwwwwwwww')
        
        ##Unoptimized Version
        #expectedResult['solution'] = 'ffrFDRRLLblBDLLUUfFFUURRUUBBUULLbuBUUUufUFruRUruRUubuuBUbuBUluLUluLUURurufUFUUURurufUFUUuurURUBubuFufulULuuubUBULulUFufulUL'
        
        #Optimized Version 
        expectedResult['solution'] = 'ffrFDRRLLblBDLLUUFUURRUUBBUULLbuBuufUFruRUruRbuuBUbuBUluLUluLUURurufUFuRurufUFrURUBubuFufulULUbUBULulUFufulUL'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_001_StringOptimizer(self):
        string = 'rFUUUUfRL'
        
        expectedResult = 'L'
        
        actualResult = solve._stringOptimizer(string)
        self.assertEqual(actualResult, expectedResult)
        
        