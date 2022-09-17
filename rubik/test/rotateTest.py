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
    #        (General single rotation instances)
    #        test 010: nominal valid cube with F rotation
    #        test 020: nominal valid cube with f rotation
    #        test 030: nominal valid cube with R rotation
    #        test 040: nominal valid cube with r rotation
    #        test 050: nominal valid cube with B rotation
    #        test 060: nominal valid cube with b rotation
    #        test 070: nominal valid cube with L rotation
    #        test 080: nominal valid cube with l rotation
    #        test 090: nominal valid cube with U rotation
    #        test 100: nominal valid cube with u rotation
    #        test 110: nominal valid cube with D rotation
    #        test 120: nominal valid cube with d rotation
    #
    #        (Unique rotation instances)
    #        test 130: nominal valid cube with missing rotation
    #        test 140: nominal valid cube with "" rotation
    #        test 150: nominal valid cube with missing 'dir' key
    #
    #        (Multiple rotation instance)
    #        test 160: nominal valid cube with multiple rotations.
    #
    #    sad paths:
    #        test 910: missing cube with valid rotation
    #        test 920: valid cube with invalid rotation
    
    def test_rotate_010_ShouldRotate_F_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'rgborogwrwbgbbrgrgoywbowrwrygwbygbyboryyggyrooybowwwoy'
        inputDict['dir'] = 'F'
        
        expectedResult = {}       
        expectedResult['cube'] = 'gorwrgrobybgrbrorgoywbowrwrygobyybyboryyggbgwgbwowwwoy'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_020_ShouldRotate_f_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'gorwrgrobybgrbrorgoywbowrwrygobyybyboryyggbgwgbwowwwoy'
        inputDict['dir'] = 'f'
    
        expectedResult = {}
        expectedResult['cube'] = 'rgborogwrwbgbbrgrgoywbowrwrygwbygbyboryyggyrooybowwwoy'
        expectedResult['status'] = 'ok'
    
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_030_ShouldRotate_R_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbgwyrwybbboggrwwwrbrwwyryygooooborryoywbgwyyoggorgbrg'
        inputDict['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['cube'] = 'bbgwygwygwgbwgbwroybrgwyyyygooooborryogwbrwybogrorwbrr'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_040_ShouldRotate_r_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbgwygwygwgbwgbwroybrgwyyyygooooborryogwbrwybogrorwbrr'
        inputDict['dir'] = 'r'
        
        expectedResult = {}
        expectedResult['cube'] = 'bbgwyrwybbboggrwwwrbrwwyryygooooborryoywbgwyyoggorgbrg'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_050_ShouldRotate_B_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'ogrwgrbwwobyoryybbrgwgorrroyryywobywgbgbbwrwbgyooyowgg'
        inputDict['dir'] = 'B'
    
        expectedResult = {}
        expectedResult['cube'] = 'ogrwgrbwwobgorgybwrgrrogorwgrybwogywyybbbwrwbgyooyoyyb'
        expectedResult['status'] = 'ok'
    
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_060_ShouldRotate_b_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'ogrwgrbwwobgorgybwrgrrogorwgrybwogywyybbbwrwbgyooyoyyb'
        inputDict['dir'] = 'b'
    
        expectedResult = {}
        expectedResult['cube'] = 'ogrwgrbwwobyoryybbrgwgorrroyryywobywgbgbbwrwbgyooyowgg'
        expectedResult['status'] = 'ok'
    
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_070_ShouldRotate_L_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'oogrbbrywbowwowgrrorooywybgwbrggobyybyyrwybbwowygrgrgg'
        inputDict['dir'] = 'L'
    
        expectedResult = {}
        expectedResult['cube'] = 'bogrbbbywbowwowgrrorroygybobgwygbyorgyywwyobwowyrrgrgg'
        expectedResult['status'] = 'ok'
    
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_080_ShouldRotate_l_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bogrbbbywbowwowgrrorroygybobgwygbyorgyywwyobwowyrrgrgg'
        inputDict['dir'] = 'l'
     
        expectedResult = {}
        expectedResult['cube'] = 'oogrbbrywbowwowgrrorooywybgwbrggobyybyyrwybbwowygrgrgg'
        expectedResult['status'] = 'ok'
     
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_090_ShouldRotate_U_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'yobgwywbgwoywrrorgoorwgryobbrgyobwyrgbwbyyrgoywbgbgrwo'
        inputDict['dir'] = 'U'
     
        expectedResult = {}
        expectedResult['cube'] = 'woygwywbgoorwrrorgbrgwgryobyobyobwyrrbggyboywywbgbgrwo'
        expectedResult['status'] = 'ok'
     
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_rotate_100_ShouldRotate_u_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'woygwywbgoorwrrorgbrgwgryobyobyobwyrrbggyboywywbgbgrwo'
        inputDict['dir'] = 'u'
    
        expectedResult = {}
        expectedResult['cube'] = 'yobgwywbgwoywrrorgoorwgryobbrgyobwyrgbwbyyrgoywbgbgrwo'
        expectedResult['status'] = 'ok'
    
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
                
    def test_rotate_110_ShouldRotate_D_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'rrryroybwgrryoyyrobbbrwgygbogbwgwgwgwwgbbbooywoooygwyr'
        inputDict['dir'] = 'D'
    
        expectedResult = {}
        expectedResult['cube'] = 'rrryroyrogrryoyygbbbbrwggwgogbwgwybwwwgbbbooyogroyywow'
        expectedResult['status'] = 'ok'
    
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_120_ShouldRotate_d_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'rrryroyrogrryoyygbbbbrwggwgogbwgwybwwwgbbbooyogroyywow'
        inputDict['dir'] = 'd'
    
        expectedResult = {}
        expectedResult['cube'] = 'rrryroybwgrryoyyrobbbrwgygbogbwgwgwgwwgbbbooywoooygwyr'
        expectedResult['status'] = 'ok'
    
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    def test_rotate_130_ShouldRotate_F_WithMissingRotation_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'rgborogwrwbgbbrgrgoywbowrwrygwbygbyboryyggyrooybowwwoy'
        #inputDict['dir'] = None

        expectedResult = {}       
        expectedResult['cube'] = 'gorwrgrobybgrbrorgoywbowrwrygobyybyboryyggbgwgbwowwwoy'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_140_ShouldRotate_F_WithEmptyRotation_OnValidNominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'rgborogwrwbgbbrgrgoywbowrwrygwbygbyboryyggyrooybowwwoy'
        inputDict['dir'] = ""

        expectedResult = {}       
        expectedResult['cube'] = 'gorwrgrobybgrbrorgoywbowrwrygobyybyboryyggbgwgbwowwwoy'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_150_ShouldRotate_F_MissingDir_OnValidNominalCube(self):

        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'rgborogwrwbgbbrgrgoywbowrwrygwbygbyboryyggyrooybowwwoy'

        expectedResult = {}       
        expectedResult['cube'] = 'gorwrgrobybgrbrorgoywbowrwrygobyybyboryyggbgwgbwowwwoy'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        

    def test_rotate_160_ShouldRotate_MultiCharDir_OnValidnominalCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        inputDict['dir'] = "FR"
    
        expectedResult = {}       
        expectedResult['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult['status'] = 'ok'
    
        actualResult = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        

        
