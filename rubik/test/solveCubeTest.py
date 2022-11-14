'''
Created on Nov 13, 2022

@author: Martin
'''

import unittest
import rubik.solve as solve

class solveCubeTest(unittest.TestCase):


    def test_solve_060a_countingHornsforTopCorners_0(self): 
        cube = 'rwowwwwwwwoyrrrrrrorryyyyyyyywoooooobbbbbbbbbggggggggg'
                        
        expectedResult = {}
        expectedResult['flag'] = 'none'
        expectedResult['hornColor'] = None
        expectedResult['hornLocation'] = None
        
        flag, hornColor, hornLocation, = solve._countHorns(cube)
        self.assertEqual(expectedResult.get('flag'), flag)
        self.assertEqual(expectedResult.get('hornColor'), hornColor)
        self.assertEqual(expectedResult.get('hornLocation'), hornLocation)
        
    def test_solve_060b_countingHornsforTopCorners_1(self):
        cube = 'roowwwwwwwwrrrrrrryryyyyyyyoywoooooobbbbbbbbbggggggggg'
                        
        expectedResult = {}
        expectedResult['flag'] = 'single'
        expectedResult['hornColor'] = 'y'
        expectedResult['hornLocation'] = 2
        
        flag, hornColor, hornLocation, = solve._countHorns(cube)
        self.assertEqual(expectedResult.get('flag'), flag)
        self.assertEqual(expectedResult.get('hornColor'), hornColor)
        self.assertEqual(expectedResult.get('hornLocation'), hornLocation)
        
    def test_solve_061a_moveHornsToBackFace(self): 
        cube = 'wwrwwwwwwyryrrrrrroywyyyyyyroooooooobbbbbbbbbggggggggg'
        hornColor = 'y'
        hornLocation = 1
        
        expectedResult = {}
        expectedResult['movementList'] = 'u'
        
        movementList = solve._moveHornsToBack(cube, hornColor, hornLocation)
        self.assertEqual(expectedResult.get('movementList'), movementList)
        
    def test_solve_062a_moveHornsToCorrectLocation(self): 
        cube = 'ywywwwwwwororrrrrrwywyyyyyyroroooooobbbbbbbbbggggggggg'
        hornColor = 'r'
        hornLocation = 3
        
        expectedResult = {}
        expectedResult['movementList'] = 'UU'
        
        movementList = solve._moveHornsToFinal(cube, hornColor, hornLocation)
        self.assertEqual(expectedResult.get('movementList'), movementList)
       
    def test_solve_063_solveTopCorners(self): 
        cube = 'roowwwwwwwrrrrrrrryyyyyyyyyowwoooooobbbbbbbbbggggggggg'
        solution = ''
        
        expectedResult = {}
        expectedResult['cube'] = list('wwwwwwwwwrorrrrrrryryyyyyyyoyooooooobbbbbbbbbggggggggg')
        expectedResult['solution'] = 'rFrBBRfrBBRRu'
        
        actualResult= solve._solveTopCorners(cube, solution)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        
        
        