'''
Created on Sep 6, 2022

@author: Martin
'''
import unittest
import rubik.rotate as rotate

class RotateTest(unittest.TestCase):

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
    #    happy paths:
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
    
    def test_rotate_010_ShouldRotateValidNominalCubeF(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'ggoybybrbwgggrrybgybwbgbyrbgoooooowwryrgyrwwbrwrowwyyo'
        inputDict['dir'] = 'F'
        
        expectedResult = {}       
        expectedResult['cube'] = 'bygrbgbyowggwrrbbgybwbgbyrbgoroowowrryrgyrwooygwowwyyo'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_020_ShouldRotateValidNominalCubef(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bygrbgbyowggwrrbbgybwbgbyrbgoroowowrryrgyrwooygwowwyyo'
        inputDict['dir'] = 'f'
    
        expectedResult = {}
        expectedResult['cube'] = 'ggoybybrbwgggrrybgybwbgbyrbgoooooowwryrgyrwwbrwrowwyyo'
        expectedResult['status'] = 'ok'
    
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))


        
