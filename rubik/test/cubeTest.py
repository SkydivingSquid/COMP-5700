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
    #        parms:    dict, mandatory, arrived validated
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
    #    happy paths: (THESE DO NOT MATCH CURRENTLY)
    #        test 010: nominal valid cube with F rotation
    #        test 020: nominal valid cube with f rotation
    #        etc, etc
    #        test 030: nominal valid cube with missing rotation
    #        test 040: valid cube with empty "" rotation
    #        test 050: nominal valid cube with missing 'dir' key
    #
    #    sad paths:
    #        test 910: missing cube with valid rotation
    #        test 920: valid cube with invalid rotation
    #


class Test(unittest.TestCase):


    def test_init_010_shouldInsantiateCube(self):
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
        cubeString = 'wwwwwwwwwgggggggggzzzzzzzzzooooooooobbbbbbbbbyyyyyyyyy'
    
        actualResults = cube.Cube.isValidCenterColors(cubeString)
    
        self.assertTrue(actualResults)
    
    # def test_cube_040__ShouldVerifyUniqueCenterColors(self):
    #     cubeString = 'wwwwwwwwwgggggggggzzzzzzzzzooooooooobbbbbbbbbyyyyyyyyy'
    #
    #     actualResults = cube.Cube.isValidCubeChar(cubeString)
    #
    #     self.assertFalse(actualResults)
    #
    # def test_cube_050__ShouldVerifyValidDirColors(self):
    #     cubeString = 'wwwwwwwwwgggggggggzzzzzzzzzooooooooobbbbbbbbbyyyyyyyyy'
    #
    #     actualResults = cube.Cube.isValidCubeChar(cubeString)
    #
    #     self.assertFalse(actualResults)
    #

        
        
        
        
        
        
        
        
        