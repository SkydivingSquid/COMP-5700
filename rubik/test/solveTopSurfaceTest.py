'''
Created on Oct 24, 2022

@author: Martin
'''
import unittest
import rubik.solve as solve

class solveTopSurfaceTest(unittest.TestCase):
    
    def test_solve_050a_checkForTopFace(self):
        cube = 'rrybbbbbbgobrrrrrrybrggggggggbooooooyyoyyyyyowwwwwwwww'
        solution = ''
    
        expectedResult = {}
        expectedResult['cube'] = list('robbbbbbbyryrrrrrrggrggggggybyoooooobyoyyygyowwwwwwwww')
        expectedResult['solution'] = 'URUrURUUrUURUrURurURUUrUURUrURUUr'
    
        actualResult= solve._solveTopFace(cube, solution)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))

    
    
    # def test_solve_051a_SolvingTheFace_ComplexScramble(self): #Integrated Test
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'wgbgbrooboyobrgowygygogbrbrybroowwyyrowwyrgrwgwygwrbyb'
    #
    #     expectedResult = {}
    #     expectedResult['cube'] = list('orbbbbbbbrbrrrrrrrggoggggggbogooooooyyyyyyyyywwwwwwwww')
    #
    #     #Optimized Version 
    #     expectedResult['solution'] = 'FFUfRRfrFDRRUUFFUURRUUBBUULuLfuuFUfuFrURluLUbUBUlULuRurufUFrURUBubbUBULulFufulULFRUrufUUFRUruRUrufUURUrURUUrUURUrURUUr'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #     self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    #


        