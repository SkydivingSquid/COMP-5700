'''
Created on Sep 6, 2022

@author: Martin
'''
import unittest
import rubik.cube as cube

    # Analysis:    Cube:    class
    #    methods:    instantiate
    #                rotate
    #                toString
    #
    # Analysis:    Cube .__init__
    #    inputs:
    #        initialCube:    string; string; len=54, [brgoyw], 9 occurrences of each, unique middle, mandatory, unvalidated
    #    outputs:
    #        side effects:    none
    #    nominal:
    #        Instance of Cube
    #    abnormal:
    #        exception
    #
    #
    # Analysis
    #    
    #    inputs:
    #            parms:    dict, mandatory, arrived validated
    #            parms['op']:    string: 'rotate', mandatory, validated
    #            parms['cube']:    string: len=54, [brgoyw], 9 of each char, unique middle, mandatory, unvalidated
    
    #            parms['dir']:    string: len >= 0, [FfBbUuDdLlRr], optional, default to F if missing, unvalidated
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
    #        test 000: instantiation of cube. 
    #        test 012: nominal cube with 54 char
    #        test 021: nominal cube with valid letters
    #        test 031: nominal cube with valid center colors
    #        test 041: nominal cube with valid dir chars
    #
    #    sad paths:
    #        test 010: abnormal cube with less than 54 char
    #        test 011: abnormal cube with greater than 54 char <-
    #        test 020: abnormal cube with invalid letters
    #        test 030: abnormal cube with duplicate center colors 
    #        test 040: abnormal cube with invalid dir char
    #        test 050: abnormal cube with more than 9 of each char <-
    #        



class Test(unittest.TestCase):


    def test_init_000_shouldInsantiateCube(self):
        incomingCube = 'gggggggggyooyooyoobbbbbbbbbrrwrrwrrwyyyyyyrrrooowwwwww'
        myCube = cube.Cube(incomingCube)
        self.assertIsInstance(myCube, cube.Cube)
        

    def test_cube_010_ShouldVerify54CharInCube(self):
        
        cubeString = 'wwwwwwwwwgggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy'
        
        actualResults = cube.Cube.isValidLengthCube(cubeString)
        
        self.assertTrue(actualResults)

    
    def test_cube_020_ShouldVerifyValidCubeChars(self):
        cubeString = 'wwwwwwwwwgggggggggrrrrrzrrrrooooooobbbbbbyyyyyyyyy'
    
        actualResults = cube.Cube.isValidCubeChar(cubeString)
    
        self.assertFalse(actualResults)
    
    def test_cube_030__ShouldVerifyUniqueCenterColors(self):
        cubeString = 'wwwwgwwwwgggggggggzzzzzzzzzooooooooobbbbbbbbbyyyyyyyyy'
    
        actualResults = cube.Cube.isValidCenterColors(cubeString)
    
        self.assertFalse(actualResults)
    
    def test_cube_040_ShouldVerifyValidDirChars(self):
        dirString = 'FLBRDUudrblfa'
    
        actualResults = cube.Cube.isValidDirChar(dirString)
    
        self.assertFalse(actualResults)
        
    def test_cube_050_ShouldVerifyValidNineofEachChar(self):
        cubeString = 'wwwwwwwwwgggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy'
    
        actualResults = cube.Cube.isNineOfEachChar(cubeString)
    
        self.assertTrue(actualResults)
    

        
        
        
        
        
        
        
        
        