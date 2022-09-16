'''
Created on Sep 15, 2022

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
#


class Test(unittest.TestCase):


    def test_init_010_shouldInsantiateCube(self):
        incomingCube = 'gggggggggyooyooyoobbbbbbbbbrrwrrwrrwyyyyyyrrrooowwwwww'
        myCube = cube.Cube(incomingCube)
        self.assertIsInstance(myCube, cube.Cube)