'''
Created on Oct 24, 2022

@author: Martin
'''
import unittest
import rubik.solve as solve

class solveTopSurfaceTest(unittest.TestCase):
    
    def test_solve_050a_checkForTopFace(self):
        cube = 'robbbbbbbyryrrrrrrggrggggggybyoooooobyoyyygyowwwwwwwww'
        solution = ''
    
        expectedResult = {}
        expectedResult['cube'] = list('bogbbbbbborbrrrrrrrbrggggggggoooooooyyyyyyyyywwwwwwwww')
        expectedResult['solution'] = 'URUrURUUrUURUrURUUrRUrURUUrUURUrURUUr'
    
        actualResult= solve._solveTopFace(cube, solution)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        
    def test_solve_051a_checkForFlag(self):
        cube = 'robbbbbbbyryrrrrrrggrggggggybyoooooobyoyyygyowwwwwwwww'
    
        expectedResult = {}
        expectedResult['corner'] = 0
        expectedResult['flag'] = 'fish'
    
        actualResult = {} 
        actualResult['corner'], actualResult['flag'] = solve._countCorners(cube)
        self.assertEqual(expectedResult.get('corner'), actualResult.get('corner'))
        self.assertEqual(expectedResult.get('flag'), actualResult.get('flag'))
        
    def test_solve_052a_SolvingTheFace_ComplexScramble(self): #Integrated Test
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wgbgbrooboyobrgowygygogbrbrybroowwyyrowwyrgrwgwygwrbyb'
    
        expectedResult = {}
        expectedResult['cube'] = list('orbbbbbbbrbrrrrrrrggoggggggbogooooooyyyyyyyyywwwwwwwww')
    
        #Optimized Version 
        expectedResult['solution'] = 'FFUfRRfrFDRRUUFFUURRUUBBUULuLfuuFUfuFrURluLUbUBUlULuRurufUFrURUBubbUBULulFufulULFRUrufUUFRUruRUrufUURUrURUUrUURUrURUUr'
        expectedResult['status'] = 'ok'
    
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('solution'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    


        