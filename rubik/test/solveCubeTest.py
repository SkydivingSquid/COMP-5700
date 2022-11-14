'''
Created on Nov 13, 2022

@author: Martin
'''

import unittest
import rubik.solve as solve

class solveCubeTest(unittest.TestCase):


    def test_solve_060a_countingHornsforTopCorners(self): #Integrated Test
        cube = ''
        flag = ''
        hornColor = ''
        hornLocation = ''
                
        expectedResult = {}
        expectedResult['flag'] = 'none'
        expectedResult['hornColor'] = 'None'
        expectedResult['hornLocation'] = 'None'
        
        flag, hornColor, hornLocation, = solve._countHorns(cube)
        self.assertEqual(expectedResult.get('flag'), flag)
        self.assertEqual(expectedResult.get('hornColor'), hornColor)
        self.assertEqual(expectedResult.get('hornLocation'), hornLocation)
        
        