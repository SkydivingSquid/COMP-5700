'''
Created on Oct 24, 2022

@author: Martin
'''
import unittest
import rubik.solve as solve

class solveTopCrossTest(unittest.TestCase):
    
    def test_solve_051_checkForTopCross(self):
        cube = 'rrybbbbbbgobrrrrrrybrggggggggbooooooyyoyyyyyowwwwwwwww'
        solution = ''
    
        expectedResult = {}
        expectedResult['cube'] = 'rrybbbbbbgobrrrrrrybrggggggggbooooooyyoyyyyyowwwwwwwww'
        expectedResult['solution'] = ''
    
        actualResult= solve._solveTopCross(cube, solution)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))


    def test_solve_052_checkForTopBar(self):
        cube = 'gyybbbbbbogorrrrrryybggggggrbrooooooyogyyyyrbwwwwwwwww'
        solution = ''
        
        expectedResult = {}
        expectedResult['cube'] = list('oogbbbbbbyryrrrrrrbgoggggggybyoooooogyryyybyrwwwwwwwww')
        expectedResult['solution'] = 'FRUruf'
        
        actualResult= solve._checkForTopBar(cube, solution)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        
    def test_solve_053_checkForTopArm(self):
        cube = 'bygbbbbbboryrrrrrrbbgggggggyyoooooooryrgyyyoywwwwwwwww'
        solution = ''
        
        expectedResult = {}
        expectedResult['cube'] = list('robbbbbbbyryrrrrrrggrggggggybyoooooobyoyyygyowwwwwwwww')
        expectedResult['solution'] = 'uFRUrufFRUruf'
        
        actualResult= solve._checkForTopArm(cube, solution)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    
    def test_solve_054_SolvingTheTopCross_ComplexScramble(self): #Integrated Test
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'obyybbowggoworroybgwgggwyyryyygorwrwrorbygbrobbwwwgbor'
    
        expectedResult = {}
        expectedResult['cube'] = list('ybybbbbbboogrrrrrryryggggggbgoooooooryryyygybwwwwwwwww')
        
        #Optimized Version 
        expectedResult['solution'] = 'LLUlFFlfLDFrFDRRFFURRBBULLruRUUfuuFUfuFUbuBUUruuRUruRUbuBluLFufulULuurURUBububUBULululULUFuRUrufUUFRUruRUruf'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))