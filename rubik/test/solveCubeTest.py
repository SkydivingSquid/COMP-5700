'''
Created on Nov 13, 2022

@author: Martin
'''

import unittest
import rubik.solve as solve

class solveCubeTest(unittest.TestCase):


    def test_solve_060a_countingHornsforTopCorners_0(self): #Integrated Test
        cube = 'rwowwwwwwwoyrrrrrrorryyyyyyyywoooooobbbbbbbbbggggggggg'
                        
        expectedResult = {}
        expectedResult['flag'] = 'none'
        expectedResult['hornColor'] = None
        expectedResult['hornLocation'] = None
        
        flag, hornColor, hornLocation, = solve._countHorns(cube)
        self.assertEqual(expectedResult.get('flag'), flag)
        self.assertEqual(expectedResult.get('hornColor'), hornColor)
        self.assertEqual(expectedResult.get('hornLocation'), hornLocation)
        
    def test_solve_060b_countingHornsforTopCorners_1(self): #Integrated Test
        cube = 'roowwwwwwwwrrrrrrryryyyyyyyoywoooooobbbbbbbbbggggggggg'
                        
        expectedResult = {}
        expectedResult['flag'] = 'single'
        expectedResult['hornColor'] = 'y'
        expectedResult['hornLocation'] = 2
        
        flag, hornColor, hornLocation, = solve._countHorns(cube)
        self.assertEqual(expectedResult.get('flag'), flag)
        self.assertEqual(expectedResult.get('hornColor'), hornColor)
        self.assertEqual(expectedResult.get('hornLocation'), hornLocation)
        
    def test_solve_061a_moveHornsToBackFace(self): #Integrated Test
        cube = 'wwrwwwwwwyryrrrrrroywyyyyyyroooooooobbbbbbbbbggggggggg'
        hornColor = 'y'
        hornLocation = 1
        
        expectedResult = {}
        expectedResult['movementList'] = 'u'
        
        movementList = solve._moveHornsToBack(cube, hornColor, hornLocation)
        self.assertEqual(expectedResult.get('movementList'), movementList)
        
        
        
        
        