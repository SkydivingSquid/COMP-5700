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
        expectedResult['cube'] = 'gyybbbbbbogorrrrrryybggggggrbrooooooyogyyyyrbwwwwwwwww'
        expectedResult['solution'] = ''
        
        actualResult= solve._checkForTopBar(cube, solution)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
    
      
    def test_solve_053_checkForTopArm(self):
        cube = 'yyobbbbbbbygrrrrrroryggggggbbgooooooryyyyorgywwwwwwwww'
        solution = ''
        
        expectedResult = {}
        expectedResult['cube'] = 'yyobbbbbbbygrrrrrroryggggggbbgooooooryyyyorgywwwwwwwww'
        expectedResult['solution'] = ''
        
        actualResult= solve._checkForTopArm(cube, solution)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))