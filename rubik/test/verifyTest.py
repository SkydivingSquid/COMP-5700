'''
Created on Sep 6, 2022

@author: Martin
'''
import unittest
import rubik.verify as verify


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass





    def test_verify_010_ShouldVerify54CharInCube(self):
        
        cubeString = 'wwwwwwwwwgggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy'
        
        actualResults = verify.isValidLengthCube(cubeString)
        
        self.assertTrue(actualResults)
